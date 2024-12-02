# ⚡️ Multimodal Chatbot with Gemini Flash

This repository hosts a Streamlit application showcasing a multimodal chatbot using Google's Gemini Flash model. The chatbot supports both text and image inputs, providing intelligent and fast responses.

## ✨ Features
Multimodal Input: Interact with the chatbot using text and/or uploaded images.
Gemini Flash Model: Leverages Google's Gemini Flash model for highly accurate and fast responses.
Chat History: Displays a conversational history for better context and seamless interaction.
Modern UI: A clean and professional user interface for an intuitive user experience.

## 🛠️ How to Get Started

### 1. Clone the Repository

git clone https://github.com/karthiksaran018/multimodal-chatbot.git
### 2. Navigate to the Project Directory

cd multimodal-chatbot
### 3. Create a Virtual Environment and Activate It

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Set Up Your API Key

Add a .env File:
In the project root directory, create a .env file and add your Google AI Studio API key like this:

GOOGLE_API_KEY=your_api_key_here

Alternatively, set up the key in Streamlit Cloud secrets if hosting online.

### 6. Run the Application

streamlit run gemini_multimodal_chatbot.py

### 7. Interact with the Chatbot

Open the link provided by Streamlit (e.g., http://localhost:8501).
Start interacting with the chatbot using text and/or image inputs.

## 🚀 Deployment on Streamlit Cloud

Push this repository to your GitHub account.
Go to Streamlit Cloud and connect your GitHub repository.
Configure the app's entry point to gemini_multimodal_chatbot.py.
Securely add your GOOGLE_API_KEY in the Secrets section.
Deploy the app and share the generated URL with others!

## 📚 Project Structure

multimodal-chatbot/

│

├── gemini_multimodal_chatbot.py  # Main Streamlit app

├── requirements.txt             # Required Python libraries

├── .env                         # Stores Google API Key (not committed)

├── README.md                    # Project documentation

└── venv/                        # Virtual environment directory (optional)


## 🌟 Credits
This project was inspired by examples from Google's Gemini Flash API and has been customized for better UI and functionality.
Updated and maintained by Karthik Saran.

## 📃 License
This project is licensed under the MIT License. See the LICENSE file for details.
