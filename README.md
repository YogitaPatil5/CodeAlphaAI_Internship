# FAQ Chatbot

## 📌 Project Overview
The **FAQ Chatbot** is a Streamlit-based application designed to provide automated responses to frequently asked questions. It leverages NLP techniques to process user queries and retrieve relevant answers from a predefined dataset.

## 📂 Project Structure
```
FAQ_CHATBOT/
│── faq_chatbot_project/
│   ├── data/
│   │   ├── faq_data.json  # JSON file containing FAQ data
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── chatbot.py  # Main chatbot logic
│   │   ├── data_loader.py  # Loads FAQ data
│   │   ├── exception.py  # Handles errors
│   │   ├── loggerfile.py  # Logs chatbot activity
│   │   ├── model.py  # NLP model logic
│   │   ├── template.py  # Text templates
│   │   ├── text_processor.py  # Text preprocessing functions
│   ├── main.py  # Main chatbot script (not used for UI)
│   ├── README.md  # Project documentation
│   ├── requirements.txt  # Python dependencies
│   ├── stapp.py  # Streamlit app file
│── venv/  # Virtual environment (optional)
│── .gitignore  # Files to ignore in Git
│── chatbot.log  # Log file
│── faq_chat_experiment.py  # Experimental chatbot script
│── LICENSE  # Project license
```

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone <repository_url>
cd FAQ_CHATBOT
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download NLP Model (if required)
If your chatbot uses `spacy` NLP models, install the required model:
```bash
python -m spacy download en_core_web_lg
```

## 🎮 Running the FAQ Chatbot
To launch the chatbot in a Streamlit web app, run:
```bash
streamlit run faq_chatbot_project/stapp.py
```

## 🛠️ Deployment Guide
To deploy the chatbot on a cloud platform like **Streamlit Sharing**, **Heroku**, or **AWS**, follow these steps:
1. Ensure all dependencies are listed in `requirements.txt`.
2. Add a `Procfile` for Heroku (if using Heroku):
   ```
   web: streamlit run faq_chatbot_project/stapp.py
   ```
3. Push the project to GitHub/GitLab.
4. Follow platform-specific deployment steps.

---
## 📧 Contact
For questions or contributions, feel free to open an issue or reach out!