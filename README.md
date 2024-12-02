# ⚡️ Multimodal Chatbot with Gemini Flash

This repository hosts a Streamlit application showcasing a multimodal chatbot using Google's Gemini Flash model. The chatbot supports both text and image inputs, providing intelligent and fast responses.

---

## ✨ Features

- **Multimodal Input**: Interact with the chatbot using text and/or uploaded images.
- **Gemini Flash Model**: Leverages Google's Gemini Flash model for highly accurate and fast responses.
- **Chat History**: Displays a conversational history for better context and seamless interaction.
- **Modern UI**: A clean and professional user interface for an intuitive user experience.

---

## 🚀 Live Demo

Try the live demo here: [Multimodal Chatbot](https://multimodal-chatbot.streamlit.app/)

---

## 🛠️ How to Get Started

### **1. Clone the Repository**
```bash
git clone https://github.com/karthiksaran018/multimodal-chatbot.git```
2. Navigate to the Project Directory
bash
Copy code
cd multimodal-chatbot
3. Create a Virtual Environment and Activate It
bash
Copy code
# Create a virtual environment
python -m venv venv

# Activate it
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
4. Install Dependencies
bash
Copy code
pip install -r requirements.txt
5. Set Up Your API Key
Add a .env File
In the project root directory, create a .env file and add your Google AI Studio API key like this:

plaintext
Copy code
GOOGLE_API_KEY=your_api_key_here
Alternatively:
If deploying on Streamlit Cloud, set the API key in the Secrets section.

6. Run the Application
bash
Copy code
streamlit run gemini_multimodal_chatbot.py
🚀 Deployment on Streamlit Cloud
1. Push the Repository to GitHub
Ensure the code is available in your GitHub account.

2. Connect to Streamlit Cloud
Go to Streamlit Cloud and connect your GitHub repository.

3. Configure the App
Set the app's entry point to gemini_multimodal_chatbot.py.

4. Add Secrets
Securely add your GOOGLE_API_KEY in the Secrets section.

5. Deploy
Deploy the app and share the generated URL with others!

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
This project was inspired by examples from Google's Gemini Flash API and has been customized for better UI and functionality.
Updated and maintained by Karthik Saran.

📃 License
This project is licensed under the MIT License. See the LICENSE file for details.
