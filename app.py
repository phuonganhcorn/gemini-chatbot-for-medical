import time
import os
import joblib
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Title and login interface
st.title("Gemini Medical Chatbot")

# Function to load keywords from a file
def load_keywords_from_file(file_path):
    keywords = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            keyword = line.strip()  # Remove whitespace and newline characters
            keywords.append(keyword)
    return keywords

# Function to check if the prompt contains medical keywords
def is_medical_issue(prompt):
    path_file = "./keywords.txt"
    medical_keywords = load_keywords_from_file(path_file)
    for keyword in medical_keywords:
        if keyword in prompt.lower():
            return True
    return False

# Login interface
api_key_input = st.text_input("Enter your API Key:")

if api_key_input:
    os.environ['GOOGLE_API_KEY'] = api_key_input
    genai.configure(api_key=api_key_input)

    new_chat_identifier = f'{time.time()}'
    assistant_role = 'assistant'
    assistant_avatar_icon = '🤖'

    user_name = st.text_input("Enter your username:")  # Define user_name here

    # Create a data/ folder if it doesn't already exist
    try:
        os.mkdir('data/')
    except:
        # data/ folder already exists
        pass

    # Load past chats (if available)
    try:
        past_chats_dictionary: dict = joblib.load('data/past_chats_list')
    except:
        past_chats_dictionary = {}

    # Sidebar allows a list of past chats
    with st.sidebar:
        st.write('# Past Chats')
        if st.session_state.get('chat_id') is None:
            st.session_state.chat_id = st.selectbox(
                label='Pick a past chat',
                options=[new_chat_identifier] + list(past_chats_dictionary.keys()),
                format_func=lambda x: past_chats_dictionary.get(x, 'New Chat'),
                placeholder='_',
            )
        else:
            # This will happen the first time AI response comes in
            st.session_state.chat_id = st.selectbox(
                label='Pick a past chat',
                options=[new_chat_identifier, st.session_state.chat_id] + list(past_chats_dictionary.keys()),
                index=1,
                format_func=lambda x: past_chats_dictionary.get(x, 'New Chat' if x != st.session_state.chat_id else st.session_state.chat_title),
                placeholder='_',
            )
        # Save new chats after a message has been sent to AI
        # TODO: Give user a chance to name chat
        st.session_state.chat_title = f'ChatSession-{st.session_state.chat_id}'

    st.write('# Chat cùng Gemini')

    # Chat history (allows to ask multiple questions)
    try:
        st.session_state.messages = joblib.load(
            f'data/{st.session_state.chat_id}-st_messages'
        )
        st.session_state.gemini_history = joblib.load(
            f'data/{st.session_state.chat_id}-gemini_messages'
        )
        print('old cache')
    except:
        st.session_state.messages = []
        st.session_state.gemini_history = []
        print('new_cache made')
    st.session_state.model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat = st.session_state.model.start_chat(
        history=st.session_state.gemini_history,
    )

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(
            name=message['role'],
            avatar=message.get('avatar'),
        ):
            st.markdown(message['content'])

    # React to user input
    if user_prompt := st.text_input('Your message here...'):
        # Save this as a chat for later
        if st.session_state.chat_id not in past_chats_dictionary.keys():
            past_chats_dictionary[st.session_state.chat_id] = st.session_state.chat_title
            joblib.dump(past_chats_dictionary, 'data/past_chats_list')
        # Display user message in chat message container
        with st.chat_message('user'):
            st.markdown(user_prompt)
        # Add user message to chat history
        st.session_state.messages.append(
            dict(
                role='user',
                content=user_prompt,
            )
        )
        ## Send message to AI
        response = st.session_state.chat.send_message(
            user_prompt,
            stream=True,
        )
        # Check if the prompt concerns medical topics
        if is_medical_issue(user_prompt):
            # Display assistant response in chat message container
            with st.chat_message(
                name=assistant_role,
                avatar=assistant_avatar_icon,
            ):
                message_placeholder = st.empty()
                full_response = ''
                assistant_response = response
                # Streams in a chunk at a time
                for chunk in response:
                    # Simulate stream of chunk
                    # TODO: Chunk missing `text` if API stops mid-stream ("safety"?)
                    for ch in chunk.text.split(' '):
                        full_response += ch + ' '
                        time.sleep(0.05)
                        # Rewrites with a cursor at end
                        message_placeholder.write(full_response + '▌')
                # Write full message with placeholder
                message_placeholder.write(full_response)

            # Add assistant response to chat history
            st.session_state.messages.append(
                dict(
                    role=assistant_role,
                    content=st.session_state.chat.history[-1].parts[0].text,
                    avatar=assistant_avatar_icon,
                )
            )
            st.session_state.gemini_history = st.session_state.chat.history
            # Save to file
            joblib.dump(
                st.session_state.messages,
                f'data/{st.session_state.chat_id}-st_messages',
            )
            joblib.dump(
                st.session_state.gemini_history,
                f'data/{st.session_state.chat_id}-gemini_messages',
            )
        else:
            # If not a medical issue, respond accordingly
            with st.chat_message(
                name=assistant_role,
                avatar=assistant_avatar_icon,
            ):
                if "chào" in user_prompt.lower():
                    st.markdown(f"Xin chào {user_name}. Tôi là Gemini Chatbot, tôi sẽ giúp bạn giải đáp các câu hỏi về lĩnh vực y tế.")
                elif "bạn là ai" in user_prompt.lower():
                    st.markdown("Tôi là Thư ký Gemini chuyên phục vụ trả lời các câu hỏi y tế.")
                else:
                    st.markdown("Tôi chỉ trả lời các câu hỏi về y tế. Bạn vui lòng hỏi lại nhé")
