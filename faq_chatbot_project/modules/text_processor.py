import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLP resources are downloaded
nltk.download('punkt')  # For tokenizing words
nltk.download('stopwords')  # For filtering common stopwords
nltk.download('wordnet')  # For lemmatization

class TextProcessor:
    """
    Handles text preprocessing tasks, including:
    - Tokenization: Splitting text into individual words (tokens)
    - Stopword Removal: Filtering out common words like 'is', 'the', 'and'
    - Lemmatization: Converting words to their root form (e.g., 'running' → 'run')
    """

    def __init__(self):
        """
        Initializes the TextProcessor by loading stopwords and setting up a lemmatizer.
        """
        try:
            self.stop_words = set(stopwords.words('english'))  # Load English stopwords
            self.lemmatizer = WordNetLemmatizer()  # Initialize lemmatizer
        except Exception as e:
            print(f"Error initializing TextProcessor: {e}")  # Handle potential errors

    def preprocess_text(self, text):
        """
        Preprocesses the input text by:
        1. Converting it to lowercase
        2. Tokenizing into words
        3. Removing punctuation and stopwords
        4. Lemmatizing words to their root form

        Parameters:
        text (str): The input sentence or phrase to preprocess.

        Returns:
        str: The cleaned and processed text as a single string.
        """
        # Convert text to lowercase and tokenize it into words
        tokens = word_tokenize(text.lower())

        # Remove stopwords and non-alphanumeric words (punctuation, special characters, etc.)
        tokens = [word for word in tokens if word.isalnum() and word not in self.stop_words]

        # Apply lemmatization to reduce words to their base form
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]

        # Join the processed tokens back into a single string
        return ' '.join(tokens)

# Test the module by processing sample sentences
if __name__ == "__main__":
    text_processor = TextProcessor()
    
    # Sample sentences for testing
    sample_sentences = [
        "Hello, how are you?",
        "I'm fine, thanks!",
        "Processing natural language is challenging!",
        "Lemmatization helps in text standardization."
    ]

    # Preprocess and print each sample sentence
    for sentence in sample_sentences:
        print(f"Original: {sentence}")
        print(f"Processed: {text_processor.preprocess_text(sentence)}\n")
