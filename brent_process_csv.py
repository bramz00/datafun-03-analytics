"""
Process a CSV file on different industry names.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "C:\\Repos\\datafun-03-analytics\\data"
PROCESSED_DIR: str = "C:\\Repos\\datafun-03-analytics\\data_processed"

#####################################
# Define Functions
#####################################

def slash_remover(file_path: pathlib.Path) -> list:
    """Removes industry names containing a slash"""
    try:
        # load data into a list
        data_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                if "\\" not in row:
                    try:
                        data_list.append(row)  # Extract and convert to float
                    except:
                        logger.warning(f"Skipping invalid row: {row}")
        return data_list
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return []

def process_csv_file():
    """Read a CSV file, remove slashes, and save the results."""
    
    input_file = pathlib.Path(FETCHED_DATA_DIR, "industry_names.csv")
    
    output_file = pathlib.Path(PROCESSED_DIR, "industry_names_no_slash.txt")
    
    # TODO: Call your new function to process YOUR CSV file
    # TODO: Create a new local variable to store the result of the function call
    modified_names = slash_remover(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:

        # TODO: Update the output to describe your results
        for object in modified_names:
            file.write(object)
    
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
