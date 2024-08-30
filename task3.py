"""Task 3: Return aggregates"""

import json

def load_json_file(input_file):
    """Load the JSON data from the file."""
    with open(input_file, 'r') as file:
        data = json.load(file)
    return data

def determine_rating_thresholds(data):
    """Determine the thresholds for different rating texts based on aggregate ratings."""
    ratings_data = {
        "Excellent": [],
        "Very Good": [],
        "Good": [],
        "Average": [],
        "Poor": []
    }
    
    # Extract the aggregate ratings and corresponding rating texts
    for record in data:
        for restaurant_record in record['restaurants']:
            restaurant = restaurant_record['restaurant']
            aggregate_rating = float(restaurant['user_rating']['aggregate_rating'])
            rating_text = restaurant['user_rating']['rating_text']
            
            # Only consider the specified rating texts
            if rating_text in ratings_data:
                ratings_data[rating_text].append(aggregate_rating)
    
    # Determine the thresholds for each rating text
    aggregates = {}
    for rating_text, ratings in ratings_data.items():
        if ratings:
            aggregates[rating_text] = {
                "min": min(ratings),
                "max": max(ratings),
                "count": len(ratings),
                "average": sum(ratings) / len(ratings),
            }
    
    return aggregates

def main():
    input_file = 'restaurant_data.json'
    
    # Load JSON data
    data = load_json_file(input_file)
    
    # Determine the rating thresholds
    rating_aggregates = determine_rating_thresholds(data)
    
    # Print the thresholds
    print('\n')
    print("Task 3: Rating Aggregates")
    print('\n')
    total_count = sum([aggregates["count"] for aggregates in rating_aggregates.values()])
    print("Total Rating Count:", total_count)
    print('\n')
    print(f"{'Rating Text':<15} {'Minimum Rating':<15} {'Maximum Rating':<15} {'Average Rating':<15} {'Percentage':<15} {'Count':<5} ")
    print('-' * 85)
    
    # Print each row of aggregates with aligned columns
    for rating_text, aggregates in rating_aggregates.items():
        aggregates["percentage"] = (aggregates["count"] / total_count) * 100
        print(f"{rating_text:<15} {aggregates['min']:<15.2f} {aggregates['max']:<15.2f} {aggregates['average']:<15.2f} {aggregates['percentage']:<15.2f} {aggregates['count']:<5}")
    print('-' * 85)
    print('* The percentage is calculated based on the count of each rating text over the total number of ratings')
    

if __name__ == '__main__':
    main()