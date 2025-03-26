import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import spacy

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class FAQChatbot:
    def __init__(self, faq_data_path):
        """
        Initialize the FAQ chatbot.
        
        Args:
            faq_data_path (str): Path to JSON file containing FAQ data
        """
        # Load FAQ data
        self.faq_dict = self.load_faq_data(faq_data_path)
        
        # Initialize NLP tools
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
        # Load spaCy model for more advanced NLP
        self.nlp = spacy.load('en_core_web_sm')
        
        # Process all FAQs for efficient matching
        self.questions = list(self.faq_dict.keys())
        self.answers = list(self.faq_dict.values())
        self.processed_questions = [self.preprocess_text(q) for q in self.questions]
        
        # Create TF-IDF vectorizer and fit it to our questions
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.processed_questions)
        
        # Define confidence threshold
        self.confidence_threshold = 0.4
    
    def load_faq_data(self, file_path):
        """Load FAQ data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading FAQ data: {e}")
            # Return some default FAQs if file loading fails
            return {
                "What is this chatbot?": "I am an FAQ chatbot built with NLP techniques.",
                "How do you work?": "I use text similarity to match your questions to predefined FAQs."
            }
    
    def preprocess_text(self, text):
        """Preprocess text by tokenizing, removing stopwords, and lemmatizing."""
        # Tokenize
        tokens = word_tokenize(text.lower())
        
        # Remove stopwords and punctuation
        tokens = [word for word in tokens if word.isalnum() and word not in self.stop_words]
        
        # Lemmatize
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
        
        return ' '.join(tokens)
    
    def find_most_similar_question(self, query):
        """Find the most similar question in the FAQ database."""
        # Preprocess the query
        processed_query = self.preprocess_text(query)
        
        # Vectorize the query
        query_vector = self.vectorizer.transform([processed_query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_vector, self.question_vectors).flatten()
        
        # Find the index of the most similar question
        max_index = np.argmax(similarities)
        max_similarity = similarities[max_index]
        
        return max_index, max_similarity
    
    def get_entity_information(self, query):
        """Extract entities from query using spaCy for more targeted responses."""
        doc = self.nlp(query)
        entities = {ent.label_: ent.text for ent in doc.ents}
        return entities
    
    def generate_response(self, query):
        """Generate a response to the user's query."""
        # Check for special commands
        if query.lower() in ["quit", "exit", "bye"]:
            return "Goodbye! Have a great day."
        
        # Find the most similar question
        best_match_index, confidence = self.find_most_similar_question(query)
        
        # Extract entities for enhanced understanding
        entities = self.get_entity_information(query)
        
        # Get the matching question for reference
        matched_question = self.questions[best_match_index]
        
        # If confidence is high enough, return the matching answer
        if confidence >= self.confidence_threshold:
            return {
                "answer": self.answers[best_match_index],
                "matched_question": matched_question,
                "confidence": confidence
            }
        else:
            # Look for entities to give more helpful response
            if entities:
                entity_info = ", ".join([f"{k}: {v}" for k, v in entities.items()])
                return {
                    "answer": f"I'm not sure I understand your question fully. I noticed you mentioned {entity_info}. Could you rephrase your question?",
                    "matched_question": None,
                    "confidence": confidence
                }
            else:
                return {
                    "answer": "I'm not sure I understand. Could you rephrase your question or provide more details?",
                    "matched_question": None,
                    "confidence": confidence
                }
    
    def save_new_question(self, question, answer):
        """Save a new question and answer to the FAQ database."""
        self.faq_dict[question] = answer
        self.questions.append(question)
        self.processed_questions.append(self.preprocess_text(question))
        self.answers.append(answer)
        
        # Update vectors
        self.question_vectors = self.vectorizer.fit_transform(self.processed_questions)
        
        # Save to file
        try:
            with open('updated_faq_data.json', 'w') as f:
                json.dump(self.faq_dict, f, indent=4)
            return "New FAQ added successfully and saved to file!"
        except Exception as e:
            return f"New FAQ added to memory but failed to save to file: {e}"
    
    def keyword_search(self, query):
        """Perform a simple keyword search as fallback."""
        query_words = set(self.preprocess_text(query).split())
        results = []
        
        for i, question in enumerate(self.processed_questions):
            question_words = set(question.split())
            common_words = query_words.intersection(question_words)
            if common_words:
                results.append((i, len(common_words) / len(question_words)))
        
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:3] if results else []
    
    def interactive_mode(self):
        """Run the chatbot in interactive mode."""
        print("FAQ Chatbot initialized. Type 'quit' to exit.")
        print("="*50)
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("Chatbot: Goodbye!")
                break
                
            response_data = self.generate_response(user_input)
            response = response_data["answer"]
            confidence = response_data["confidence"]
            
            print(f"Chatbot: {response}")
            
            # If confidence is low, suggest alternatives
            if confidence < self.confidence_threshold:
                fallback_results = self.keyword_search(user_input)
                if fallback_results:
                    print("Did you mean one of these?")
                    for i, (idx, score) in enumerate(fallback_results, 1):
                        print(f"{i}. {self.questions[idx]}")
                    
                    selection = input("Enter number to select, or 'n' to add as new question: ")
                    if selection.isdigit() and 1 <= int(selection) <= len(fallback_results):
                        idx = fallback_results[int(selection)-1][0]
                        print(f"Chatbot: {self.answers[idx]}")
                    elif selection.lower() == 'n':
                        answer = input("Please provide the answer for this question: ")
                        result = self.save_new_question(user_input, answer)
                        print(f"Chatbot: {result}")


# Demo usage
if __name__ == "__main__":
    # Initialize the chatbot with the FAQ data
    chatbot = FAQChatbot('faq_data.json')
    
    # Example queries
    test_queries = [
        "What's your return policy?",
        "How do I send something back?",
        "Do you offer international shipping?",
        "What's the warranty on your products?",
        "How can I track my package?"
    ]
    
    print("Testing chatbot with sample queries:")
    for query in test_queries:
        response = chatbot.generate_response(query)
        print(f"Q: {query}")
        print(f"A: {response['answer']}")
        if response['matched_question']:
            print(f"Matched: {response['matched_question']} (Confidence: {response['confidence']:.2f})")
        print("="*50)
    
    # Start interactive mode
    print("\nStarting interactive mode:")
    chatbot.interactive_mode()
