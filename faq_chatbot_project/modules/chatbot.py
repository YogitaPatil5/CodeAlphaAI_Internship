import logging
import os
import sys

# ✅ Setup logging
log_directory = os.path.dirname(os.path.abspath(__file__))  # Log file in modules folder
log_file_path = os.path.join(log_directory, "chatbot.log")

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# ✅ Get the absolute path of the project root & add it to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# ✅ Import required modules
from modules.data_loader import load_faq_data, save_faq_data
from modules.text_processor import TextProcessor
from modules.model import FAQModel
from modules.exception import FAQException


class FAQChatbot:
    """
    Main chatbot class for handling FAQ-based queries using machine learning.
    """

    def __init__(self, faq_file=None, confidence_threshold=0.4):
        """
        Initializes the chatbot.

        :param faq_file: Path to the FAQ JSON file (optional).
        :param confidence_threshold: Minimum confidence required to return a valid answer.
        """
        try:
            logging.info("Initializing chatbot...")

            # ✅ Ensure the FAQ file is provided
            if not faq_file:
                raise FAQException("No FAQ file provided. Please check the path.")

            # ✅ Load FAQ data correctly
            self.faq_data = load_faq_data()  # ✅ Fix: Pass the file path

            if not self.faq_data:
                raise FAQException("FAQ data is empty. Please check the data file.")

            # ✅ Extract questions & answers
            self.questions = [entry["question"] for entry in self.faq_data]
            self.answers = [entry["answer"] for entry in self.faq_data]

            # ✅ Initialize text processor & preprocess questions
            self.text_processor = TextProcessor()
            processed_questions = [self.text_processor.preprocess_text(q) for q in self.questions]

            # ✅ Initialize ML model for matching using ORIGINAL questions
            self.model = FAQModel(self.questions)  # ✅ Fix: Pass only original questions

            # ✅ Set confidence threshold
            self.confidence_threshold = confidence_threshold

            logging.info("Chatbot successfully initialized.")

        except Exception as e:
            logging.error(f"Error initializing chatbot: {e}")
            raise FAQException("Failed to initialize chatbot", cause=e)

    def generate_response(self, query):
        """
        Generates a response to a user query.

        :param query: The user's input question.
        :return: A dictionary containing:
            - "answer": The chatbot's response.
            - "matched_question": The best-matching FAQ question (if any).
            - "confidence": The confidence score.
        """
        try:
            if not query.strip():
                return {
                    "answer": "Please enter a valid question.",
                    "matched_question": None,
                    "confidence": 0.0
                }

            # ✅ Preprocess the user query
            processed_query = self.text_processor.preprocess_text(query)

            # ✅ Find the best match using the ML model
            best_match, confidence = self.model.find_best_match(processed_query)

            # ✅ Return the answer if confidence is high enough
            if confidence >= self.confidence_threshold:
                answer = self.answers[self.questions.index(best_match)]  # ✅ Fix: Correct way to get the answer
                return {
                    "answer": answer,
                    "matched_question": best_match,
                    "confidence": confidence
                }

            # ✅ Handle low-confidence cases
            return {
                "answer": "I'm not sure I understand your question fully. Could you rephrase it?",
                "matched_question": None,
                "confidence": confidence
            }

        except Exception as e:
            logging.error(f"Error generating response: {e}")
            raise FAQException("Failed to generate response", cause=e)


if __name__ == "__main__":
    """
    Runs a simple test if chatbot.py is executed directly.
    """
    try:
        # ✅ Define FAQ data path
        faq_file_path = os.path.join(os.path.dirname(__file__), "../data/faq_data.json")

        # ✅ Initialize chatbot
        chatbot = FAQChatbot(faq_file_path)

        # ✅ Test chatbot with a sample query
        sample_query = "What's your return policy?"
        response = chatbot.generate_response(sample_query)

        # ✅ Print chatbot response
        print(f"User: {sample_query}")
        print(f"Chatbot: {response['answer']} (Matched: {response['matched_question']}, Confidence: {response['confidence']:.2f})")

    except FAQException as e:
        print(f"Error: {e}")
