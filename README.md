# Gemini Medical Chatbot
---
- _A little demo with chatbot_
  
![_**A little demo with chatbot**_](https://i.imgur.com/2uobQtE.png)
- _Chatbot won't reponse with questions that not related to medical field_
  
![_**Chatbot won't reponse with questions that not related to medical field**_](https://i.imgur.com/ZTyRt7L.png)

---


## Overview 

> [!NOTE]
> - This repository utilizes the API key from Gemini. To obtain your API key, please visit [Google AI Studio](https://ai.google.dev/tutorials/workspace_auth_quickstart).
> - This repository contains LICENSE from Apache License 2.0.

The Gemini Medical Chatbot is designed to be a Vietnamese chatbot specifically tailored for the medical field. It _**leverages the API key from Google's Gemini chatbot service to provide intelligent responses to user queries related to medical topics.**_

---
## Purpose
The primary purpose of the Gemini Medical Chatbot is to assist users with medical inquiries, providing them with relevant information, advice, and guidance related to various health issues, medications, treatments, and healthcare facilities.

---
## Features
- **_Vietnamese Language Support_**: The chatbot only capable of responding to user queries in the Vietnamese language, enhancing accessibility for Vietnamese-speaking users.
- **_Integration with Google's Gemini Chatbot API_**: The chatbot utilizes the API key from Google's Gemini chatbot service, allowing it to access advanced natural language processing capabilities and provide accurate responses to user queries.
- **_Medical Topic Understanding_**: The chatbot is specifically trained with specific prompt keywords to understand and respond only to queries related to medical topics. It can identify keywords and phrases commonly associated with health, healthcare facilities, medical conditions, treatments, and more.
- **_Streamlit User Interface_**: The chatbot features a user-friendly interface built using Streamlit, a Python library for creating web applications. Users can interact with the chatbot directly through the web interface, entering their queries and receiving responses in real-time.
- **_Chat History Management_**: The chatbot maintains a history of past conversations, allowing users to review previous interactions and continue ongoing conversations seamlessly.

---
## Implementation
The Gemini Medical Chatbot is implemented using Python programming language and various libraries and frameworks, including ```Streamlit``` for the user interface and the ```Google Gemini Chatbot API``` for natural language processing capabilities.

_First, clone this repository to your computer and then follow the instructions below._
### Step 1: Creat virtual/conda environment
- _With virtual environment_
```
python -m venv gemini-chatbot
source gemini-chatbot/bin/activate #for ubuntu
gemini-chatbot/Scripts/activate #for windows
```
- _With conda environment_
```
conda create --name gemini-chatbot
```
_After the installation, run command below to activate conda environment_
```
conda activate gemini-chatbot
```

### Step 2: Install libraries
```
cd ./Gemini-Medical-Chatbot
pip install -r requirements.txt
```

### Step 3: Run chatbot interface with Streamlit
```
streamlit run app.py
```
---

> [!NOTE]
> - This chatbot right now just answer to questions related to medical topic and in Vietnamese, this is because of ```keywords.txt```. Users can modify this with English keywords or any other languages.
> - To ensure that the model responds only within the scope of the medical field, I have created a file containing keywords related to the medical topic. Users can update ```keywords.txt``` file after cloning this repository to enhance the accuracy/flexibility of the chatbot.
