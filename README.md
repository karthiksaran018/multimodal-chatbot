# ⚡️ Multimodal Chatbot with Gemini Flash

This repository hosts a Streamlit application showcasing a multimodal chatbot using Google's Gemini Flash model. The chatbot supports both text and image inputs, providing intelligent and fast responses.

## ✨ Features

- **Multimodal Input**: Interact with the chatbot using text and/or uploaded images.
- **Gemini Flash Model**: Leverages Google's Gemini Flash model for highly accurate and fast responses.
- **Chat History**: Displays a conversational history for better context and seamless interaction.
- **Modern UI**: A clean and professional user interface for an intuitive user experience.

## 🚀 Live Demo

Try the live demo here: [Multimodal Chatbot](https://multimodal-chatbot.streamlit.app/)

## 🛠️ How to Get Started

### Clone the Repository
```bash
git clone https://github.com/karthiksaran018/multimodal-chatbot.git

### Navigate to the Project Directory
```bash
cd multimodal-chatbot
Create a Virtual Environment and Activate It
bash
Copy code
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Set Up Your API Key
Add a .env File
In the project root directory, create a .env file and add your Google AI Studio API key like this:

plaintext
Copy code
GOOGLE_API_KEY=your_api_key_here
Alternatively:
If deploying on Streamlit Cloud, set the API key in the Secrets section.

Run the Application
bash
Copy code
streamlit run gemini_multimodal_chatbot.py
Interact with the Chatbot
Open the link provided by Streamlit (e.g., http://localhost:8501). Start interacting with the chatbot using text and/or image inputs.

📚 Project Structure
plaintext
Copy code
multimodal-chatbot/
├── gemini_multimodal_chatbot.py  # Main Streamlit app
├── requirements.txt             # Required Python libraries
├── .env.example                 # Example for storing the API key
├── README.md                    # Project documentation
└── venv/                        # Virtual environment directory (optional)
🌟 Credits
This project was inspired by examples from Google's Gemini Flash API and has been customized for better UI and functionality. Updated and maintained by Karthik Saran.

📃 License
This project is licensed under the MIT License. See the LICENSE file for details.
