# FAQ Chatbot

A modular, reusable FAQ chatbot built with natural language processing techniques that can answer frequently asked questions about any topic or product.

## Features

- Natural language understanding for user queries
- Customizable FAQ knowledge base via JSON files
- Interactive command-line interface
- Extendable architecture for integration with other platforms
- High accuracy question matching using TF-IDF and cosine similarity
- Easy to configure and extend

## Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Setup

1. Clone the repository or download the source code:

```bash
git clone https://github.com/yourusername/faq-chatbot.git
cd faq-chatbot
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. For development installation:

```bash
pip install -e .
```

## Quick Start

```python
from faq_chatbot.chatbot import FAQChatbot

# Initialize with default dataset
chatbot = FAQChatbot()

# Or specify your own FAQ dataset
# chatbot = FAQChatbot(faq_file='path/to/your/faqs.json')

# Start interactive mode
chatbot.chat()

# Or get a single response
response = chatbot.generate_response("What is your return policy?")
print(response)
```

## Using Your Own FAQ Dataset

Create a JSON file with your questions and answers:

```json
{
    "What is the capital of France?": "The capital of France is Paris.",
    "Who wrote Hamlet?": "William Shakespeare wrote Hamlet.",
    "What is the speed of light?": "The speed of light in a vacuum is approximately 299,792,458 meters per second."
}
```

Then load it into the chatbot:

```python
chatbot = FAQChatbot(faq_file='path/to/your/faqs.json')
```

## Command-Line Interface

The chatbot can be used directly from the command line:

```bash
python -m faq_chatbot
```

Available commands in interactive mode:
- `quit`: Exit the chatbot
- `add`: Add a new FAQ
- `save`: Save FAQs to a file
- `import`: Import FAQs from a file
- `list`: List all available FAQs

## How It Works

1. **Text Preprocessing**: Each user query is tokenized, stripped of stopwords, and lemmatized.
2. **Vectorization**: The preprocessed text is converted to a TF-IDF vector.
3. **Similarity Matching**: The vector is compared to all FAQ questions using cosine similarity.
4. **Response Generation**: The answer corresponding to the most similar question is returned.

## Project Structure

- `faq_chatbot/`: Main package
  - `nlp_processor.py`: Text processing and similarity matching
  - `faq_manager.py`: FAQ database operations
  - `chatbot.py`: Core chatbot functionality
  - `utils.py`: Utility functions
- `data/`: Data files including default FAQs
- `examples/`: Example scripts demonstrating usage

## Extending the Chatbot

### Adding Custom Response Types

You can extend the `generate_response` method in a subclass:

```python
from faq_chatbot.chatbot import FAQChatbot

class MyCustomChatbot(FAQChatbot):
    def generate_response(self, user_input):
        # Add your custom logic here
        if "special_query" in user_input.lower():
            return "This is a special response!"
        
        # Fall back to the standard response
        return super().generate_response(user_input)
```

### Integration with Other Platforms

The modular design makes it easy to integrate with web frameworks, messaging platforms, etc.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NLTK for natural language processing tools
- scikit-learn for machine learning utilities
