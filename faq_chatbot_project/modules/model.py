from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy

class FAQModel:
    """
    Handles FAQ similarity matching using a hybrid approach:
    1. TF-IDF Vectorization + Cosine Similarity
    2. Spacy's Word Vector Similarity
    3. Combines both methods for better accuracy
    """

    def __init__(self, questions):
        """
        Initializes the FAQModel with FAQ questions.
        
        Parameters:
        - questions (list): List of FAQ questions to be matched.
        """
        # ✅ Load Spacy's large model for better word vector similarity
        self.nlp = spacy.load('en_core_web_lg')  # Better accuracy than 'en_core_web_md'
        self.questions = list(set(questions))  # ✅ Remove duplicates from the FAQ list

        print("Processing Questions:", self.questions)  # Debugging assistance
        
        # ✅ TF-IDF Vectorizer with bigrams & trigrams (improves phrase matching)
        self.vectorizer = TfidfVectorizer(ngram_range=(1,3), stop_words='english')

        # ✅ Convert FAQ questions into TF-IDF vectors
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def find_best_match(self, query):
        """
        Finds the best matching FAQ for the given user query.
        
        Parameters:
        - query (str): User's input question.
        
        Returns:
        - best_match (str): The most relevant FAQ question.
        - confidence (float): Similarity score (0 to 1, higher is better).
        """
        # ✅ Get similarity scores from both methods
        tfidf_match, tfidf_conf = self.find_best_match_tfidf(query)
        spacy_match, spacy_conf = self.find_best_match_spacy(query)

        # ✅ Hybrid approach: Adjusted weight (Spacy now has more influence)
        final_conf = (0.4 * tfidf_conf) + (0.6 * spacy_conf)

        # ✅ Select the match with the **higher confidence score**
        best_match = tfidf_match if tfidf_conf > spacy_conf else spacy_match

        return best_match, final_conf

    def find_best_match_tfidf(self, query):
        """
        Finds the best FAQ match using TF-IDF + Cosine Similarity.
        
        Parameters:
        - query (str): User's input question.
        
        Returns:
        - best_match (str): Closest matching FAQ.
        - confidence (float): Similarity score (higher means better match).
        """
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.question_vectors).flatten()
        max_index = np.argmax(similarities)

        return self.questions[max_index], similarities[max_index]

    def find_best_match_spacy(self, query):
        """
        Finds the best FAQ match using Spacy's word vector similarity.
        
        Parameters:
        - query (str): User's input question.
        
        Returns:
        - best_match (str): Closest matching FAQ.
        - confidence (float): Similarity score (higher means better match).
        """
        query_doc = self.nlp(query)
        scores = [query_doc.similarity(self.nlp(q)) for q in self.questions]
        max_index = np.argmax(scores)

        return self.questions[max_index], scores[max_index]

    def extract_entities(self, query):
        """
        Extracts named entities (like dates, amounts, locations) from the query using Spacy.
        
        Parameters:
        - query (str): User's input question.
        
        Returns:
        - entities (dict): Dictionary of detected entities {EntityType: EntityText}.
        """
        doc = self.nlp(query)
        return {ent.label_: ent.text for ent in doc.ents}

if __name__ == "__main__":
    # ✅ Updated FAQ dataset with **more refund-related questions**
    sample_questions = [
        "How do I return an item?", 
        "What is your refund policy?", 
        "Can I track my order?", 
        "How long does shipping take?",
        "How do I exchange a product?",
        "Where is my package?",
        "Can I get my money back?",
        "How do I request a refund?",
        "What happens if my order is lost?"
    ]

    # ✅ Initialize the model with the hybrid approach
    model = FAQModel(sample_questions)

    # ✅ Test with a **refund-related query**
    query = "How do I get a refund?"
    best_match, confidence = model.find_best_match(query)
    
    print(f"\nUser Query: {query}")
    print(f"Best Match: {best_match}")
    print(f"Confidence Score: {confidence:.2f}")
