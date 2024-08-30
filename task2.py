"""Task 2: Extract the list of restaurants that have past event in the month of April 2019 
and store the data as restaurant_events.csv."""

import json
import csv

def load_json_file(input_file):
    """Load the JSON data from the file."""
    with open(input_file, 'r') as file:
        data = json.load(file)
    return data

def extract_restaurant_events(data):
    """Extract the list of restaurants that have past event in the month of April 2019."""
    extracted_data = []
    for record in data:
        for restaurant_record in record['restaurants']:
            restaurant = restaurant_record['restaurant']
            restaurant_id = restaurant['id']
            restaurant_name = restaurant['name']
            # Check if the restaurant has events
            if 'zomato_events' in restaurant:
                events = restaurant['zomato_events']
                for event in events:
                    event_id = event['event']['event_id'] 
                    if 'photos' in event['event'] and len(event['event']['photos']) > 0:
                        photo_url = event['event']['photos'][0]['photo']['url'] 
                    else:
                        photo_url = 'NA'
                    event_title = event['event']['title']
                    event_start_date = event['event']['start_date']
                    event_end_date = event['event']['end_date'] 
                    # Check if the event overlaps with April 2019
                    if event_start_date <= '2019-04-30' and event_end_date >= '2019-04-01':
                        extracted_data.append([
                            event_id,
                            restaurant_id,
                            restaurant_name,
                            photo_url,
                            event_title,
                            event_start_date,
                            event_end_date
                        ])
    return extracted_data

def write_to_csv(output_file, data):
    """Write the extracted data to a CSV file."""
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        # Write the header
        writer.writerow([
            'Event Id',
            'Restaurant Id', 
            'Restaurant Name',
            'Photo URL',
            'Event Title',
            'Event Start Date', 
            'Event End Date',
        ])
        # Write the extracted data
        writer.writerows(data)

def main():
    input_file = 'restaurant_data.json'
    output_file = 'restaurant_events.csv'
    
    # Load JSON data
    data = load_json_file(input_file)
    
    # Extract the list of restaurants that have past event in the month of April 2019
    extracted_data = extract_restaurant_events(data)
    
    # Write the extracted data to a CSV file
    write_to_csv(output_file, extracted_data)

    print(f"Task 2: Data has been successfully written to {output_file}")


if __name__ == '__main__':
    main()