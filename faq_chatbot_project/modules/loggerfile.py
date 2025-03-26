import logging
import os

# Get the directory of the current script (modules folder)
log_directory = os.path.dirname(os.path.abspath(__file__))  
log_file_path = os.path.join(log_directory, 'chatbot.log')  # Log file inside the modules folder

def setup_logging():
    """
    Sets up logging configuration for the chatbot.
    
    - Logs will be stored in `chatbot.log` inside the modules folder.
    - Log level is set to INFO (can be changed to DEBUG for more details).
    - Log format includes timestamp, log level, and message.
    """
    logging.basicConfig(
        filename=log_file_path,  # Log file location
        level=logging.INFO,  # Log only INFO level and above messages
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
        force=True  # Ensures reconfiguration if logging was set elsewhere
    )

if __name__ == "__main__":
    setup_logging()  # Initialize logging
    logger = logging.getLogger(__name__)  # Create a logger instance
    logger.info("Logging system initialized.")  # Log an informational message

    # Print log file path for confirmation
    print(f"Log file is saved at: {log_file_path}")  
