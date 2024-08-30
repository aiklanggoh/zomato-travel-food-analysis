"""Task 1: Extract the following fields and store the data as restaurants.csv. """

"""Import the required libraries."""
import json
import csv
import pandas as pd

def load_json_file(input_file):
    """Load the JSON data from the file."""
    with open(input_file, 'r') as file:
        data = json.load(file)
    return data