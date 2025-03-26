import os
import logging

def create_project_structure():
    """
    Creates the folder and file structure for the FAQ Chatbot Project.
    This ensures that all necessary directories and files are present.
    """
    project_name = "faq_chatbot_project"
    directories = [
        f"{project_name}/data",        # Directory for storing FAQ data
        f"{project_name}/modules"      # Directory for modular Python files
    ]
    files = {
        f"{project_name}/data/faq_data.json": "{}",  # Initializes an empty JSON file for FAQs
        f"{project_name}/modules/__init__.py": "",  # Marks modules as a package
        f"{project_name}/modules/data_loader.py": "# Module to handle loading and saving FAQ data\n\n", 
        f"{project_name}/modules/text_processor.py": "# Module for text preprocessing, tokenization, and lemmatization\n\n",
        f"{project_name}/modules/model.py": "# Module for question similarity detection using NLP\n\n",
        f"{project_name}/modules/chatbot.py": "# Core chatbot logic that interacts with users\n\n",
        f"{project_name}/modules/exception.py": "# Custom exception handling for chatbot errors\n\n",
        f"{project_name}/modules/logging.py": "# Configures logging for the chatbot\n\n",
        f"{project_name}/modules/template.py": "# Generates initial project structure\n\n",
        f"{project_name}/main.py": (
            "# Main script to run the chatbot interactively\n\n"
            "if __name__ == '__main__':\n"
            "    print('Chatbot running...')"
        ),
        f"{project_name}/requirements.txt": "# Lists dependencies required for the chatbot\n\n",
        f"{project_name}/README.md": "# Documentation for the FAQ Chatbot Project\n\n"
    }
    
    # Setup logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Check and create directories
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            logging.info(f"Created directory: {directory}")
    
    # Create files if they do not exist
    for file_path, content in files.items():
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            logging.info(f"Created file: {file_path}")

    print(f"Project structure for '{project_name}' is set up successfully.")

if __name__ == "__main__":
    create_project_structure()
