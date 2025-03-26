# Runs the chatbot interactively
import logging
from modules.chatbot import FAQChatbot
from modules.loggerfile import setup_logging

def main():
    setup_logging()
    chatbot = FAQChatbot('data/faq_data.json')
    logging.info("Chatbot initialized.")
    print("FAQ chatbot initialized. Type 'quit' to exit.")
    print("=" * 50)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
            
        response_data = chatbot.generate_response(user_input)
        response = response_data["answer"]
        confidence = response_data["confidence"]
        
        print(f"Chatbot: {response}")
        
        # ✅ Handle low confidence responses without keyword search
        if confidence < chatbot.confidence_threshold:
            print("I'm not sure. Could you clarify?")

if __name__ == '__main__':
    main()
    logging.info("Chatbot exited.")
    print("Chatbot exited.")
    print("=" * 50)
