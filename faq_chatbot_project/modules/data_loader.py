import os
import json
import logging

# Configure logging to record any errors that occur during data loading or saving
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def load_faq_data():
    """
    Load FAQ data from a JSON file dynamically, ensuring it works regardless of execution location.

    Returns:
        dict: A dictionary containing the loaded FAQ data.
              Returns an empty dictionary if an error occurs.
    """
    # Get the directory of the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the correct path to faq_data.json (going up one level to the 'data' directory)
    file_path = os.path.join(base_dir, "..", "data", "faq_data.json")

    # Print the file path for debugging
    print(f"Loading data from: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)  # Load JSON data from file and return as a dictionary
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in file: {file_path}")
        return {}
    except Exception as e:
        logging.error(f"Error loading FAQ data: {e}")
        return {}

def save_faq_data(faq_dict):
    """
    Save updated FAQ data to a JSON file dynamically.

    Parameters:
        faq_dict (dict): Dictionary containing FAQ data to be saved.

    Returns:
        None
    """
    # Get the directory of the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the correct path to faq_data.json (going up one level to the 'data' directory)
    file_path = os.path.join(base_dir, "..", "data", "faq_data.json")

    # Print the file path for debugging
    print(f"Saving data to: {file_path}")

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(faq_dict, file, indent=4)  # Save dictionary as formatted JSON
    except Exception as e:
        logging.error(f"Error saving FAQ data: {e}")

# Test the module by loading FAQ data if executed directly
if __name__ == "__main__":
    faq_data = load_faq_data()  # Load FAQ data
    print(faq_data)  # Print loaded data for verification
