import os
from pathlib import Path

def create_structure():
    base_dir = "faq_chatbot"
    structure = [
        "README.md",
        "requirements.txt",
        "setup.py",
        "faq_chatbot/__init__.py",
        "faq_chatbot/config.py",
        "faq_chatbot/nlp_processor.py",
        "faq_chatbot/faq_manager.py",
        "faq_chatbot/chatbot.py",
        "faq_chatbot/utils.py",
        "data/default_faqs.json",
        "examples/basic_usage.py",
        "examples/custom_dataset.py",
        "tests/__init__.py",
        "tests/test_nlp_processor.py",
        "tests/test_faq_manager.py",
        "tests/test_chatbot.py",
    ]

    # Create directories and files
    for item in structure:
        path = Path(base_dir) / item
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
            print(f"Created: {path}")
        else:
            print(f"Already exists: {path}")

    print("Project structure creation process completed!")

if __name__ == "__main__":
    create_structure()
