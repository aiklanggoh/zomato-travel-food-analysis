"""Task 2: Extract the list of restaurants that have past event in the month of April 2019 
and store the data as restaurant_events.csv."""

import json
import csv
import datetime

def load_json_file(input_file):
    """Load the JSON data from the file."""
    with open(input_file, 'r') as file:
        data = json.load(file)
    return data