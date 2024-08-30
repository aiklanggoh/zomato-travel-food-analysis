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

def load_country_codes(country_file):
    """Load the country codes from the file into a dictionary using Pandas."""
    # Convert Country-Code.xlsx to a dictionary
    country_codes = pd.read_excel(country_file)
    country_codes_dict = country_codes.set_index('Country Code')['Country'].to_dict()
    return country_codes_dict