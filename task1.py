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

def extract_restaurant_data(data, country_codes_dict):
    """Extract the required fields from the restaurant data."""
    extracted_data = []
    for record in data:
        for restaurant_record in record['restaurants']:
            restaurant = restaurant_record['restaurant']
            restaurant_id = restaurant['id']
            restaurant_name = restaurant['name']
            country = restaurant['location']['country_id']
            city = restaurant['location']['city']
            user_rating_votes = restaurant['user_rating']['votes']
            user_aggregate_rating = float(restaurant['user_rating']['aggregate_rating'])
            cuisines = restaurant['cuisines']
            if country in country_codes_dict:
                country = country_codes_dict[country]
            extracted_data.append([
                restaurant_id,
                restaurant_name,
                country,
                city,
                user_rating_votes,
                user_aggregate_rating,
                cuisines
            ])
    return extracted_data