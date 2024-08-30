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

def write_to_csv(output_file, data):
    """Write the extracted data to a CSV file."""
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Write the header
        writer.writerow([
            'Restaurant Id', 
            'Restaurant Name', 
            'Country', 
            'City', 
            'User Rating Votes', 
            'User Aggregate Rating', 
            'Cuisines'
        ])
        # Write the extracted data
        writer.writerows(data)

def main():
    input_file = 'restaurant_data.json'
    output_file = 'restaurants.csv'
    country_file = 'Country-Code.xlsx'
    
    # Load JSON data
    data = load_json_file(input_file)

    # Load country codes
    country_codes = load_country_codes(country_file)
    
    # Extract required restaurant data
    extracted_data = extract_restaurant_data(data, country_codes)
    
    # Write extracted data to CSV
    write_to_csv(output_file, extracted_data)
    
    print(f"Task 1: Data has been successfully written to {output_file}")

if __name__ == "__main__":
    main()