import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class FAQException(Exception):
    """
    Custom exception class for handling errors in the chatbot.
    """

    def __init__(self, message, cause=None):
        """
        Initializes the FAQException with a custom error message.
        """
        super().__init__(message)
        self.message = message
        self.cause = cause

    def __str__(self):
        """
        Returns a user-friendly string representation of the exception.
        """
        if self.cause:
            return f"{self.message} (Caused by: {repr(self.cause)})"
        return self.message

    def __repr__(self):
        """
        Returns a developer-friendly string representation of the exception.
        """
        return f"FAQException('{self.message}')"

if __name__ == "__main__":
    # Example usage
    try:
        try:
            raise ValueError("A lower-level error occurred")
        except ValueError as e:
            raise FAQException("Custom chatbot error", cause=e)
    except FAQException as e:
        logging.error(f"Handled Exception: {e}")  # Logs only here
        print(f"Caught an exception: {e}")
