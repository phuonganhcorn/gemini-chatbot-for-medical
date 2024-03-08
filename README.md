# Gemini-Medical-Chatbot

![Imgur](https://i.imgur.com/2uobQtE.png)
![Imgur](https://i.imgur.com/TfngdBg.png)

## Overview 
The Gemini Medical Chatbot is designed to be a Vietnamese chatbot specifically tailored for the medical field. It _**leverages the API key from Google's Gemini chatbot service to provide intelligent responses to user queries related to medical topics.**_

## Purpose
The primary purpose of the Gemini Medical Chatbot is to assist users with medical inquiries, providing them with relevant information, advice, and guidance related to various health issues, medications, treatments, and healthcare facilities.

## Features
- Vietnamese Language Support: The chatbot is capable of understanding and responding to user queries in the Vietnamese language, enhancing accessibility for Vietnamese-speaking users.
- Integration with Google's Gemini Chatbot API: The chatbot utilizes the API key from Google's Gemini chatbot service, allowing it to access advanced natural language processing capabilities and provide accurate responses to user queries.
- Medical Topic Understanding: The chatbot is specifically trained with specific prompt keywords to understand and respond only to queries related to medical topics. It can identify keywords and phrases commonly associated with health, healthcare facilities, medical conditions, treatments, and more.
- Streamlit User Interface: The chatbot features a user-friendly interface built using Streamlit, a Python library for creating web applications. Users can interact with the chatbot directly through the web interface, entering their queries and receiving responses in real-time.
- Chat History Management: The chatbot maintains a history of past conversations, allowing users to review previous interactions and continue ongoing conversations seamlessly.

## Implementation
The Gemini Medical Chatbot is implemented using Python programming language and various libraries and frameworks, including ```Streamlit``` for the user interface and the ```Google Gemini Chatbot API``` for natural language processing capabilities.

First, clone this repository to your computer and then follow the instructions below.
#### Step 1: Creat virtual/conda environment
- With virtual environment
```
python -m venv venv
source venv/bin/activate #for ubuntu
venv/Scripts/activate #for windows
```
- With conda environment
```
conda create --name gemini-chatbot
```
After the installation, run command below to activate conda environment
```
conda activate gemini-chatbot
```

#### Step 2: Install libraries
```
pip install -r requirements.txt
```

#### Step 3: Run chatbot interface with Streamlit
```
streamlit run app.py
```
