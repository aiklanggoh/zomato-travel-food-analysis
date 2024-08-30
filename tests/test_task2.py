import unittest
import json
import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task2 import load_json_file, extract_restaurant_events, write_to_csv


class TestTask2(unittest.TestCase):
    
    def test_load_json_file(self):
        """Test loading JSON file"""
        test_data = [{'key': 'value'}]
        with open('test_data.json', 'w') as file:
            json.dump(test_data, file)
        
        result = load_json_file('test_data.json')
        self.assertEqual(result, test_data)

        os.remove('test_data.json')

    def test_extract_restaurant_events(self):
        """Test extracting restaurant events"""
        mock_data = [
            {
                'restaurants': [
                    {
                        'restaurant': {
                            'id': 1,
                            'name': 'Restaurant 1',
                            'zomato_events': [
                                {
                                    'event': {
                                        'event_id': 1,
                                        'photos': [{'photo': {'url': 'photo1.jpg'}}],
                                        'title': 'Event 1',
                                        'start_date': '2019-03-01',
                                        'end_date': '2019-03-31'
                                    }
                                },
                                {
                                    'event': {
                                        'event_id': 2,
                                        'photos': [{'photo': {'url': 'photo2.jpg'}}],
                                        'title': 'Event 2',
                                        'start_date': '2019-04-01',
                                        'end_date': '2019-04-30'
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        ]
        result = extract_restaurant_events(mock_data)
        expected_result = [
            [2, 1, 'Restaurant 1', 'photo2.jpg', 'Event 2', '2019-04-01', '2019-04-30']
        ]
        self.assertEqual(result, expected_result)

    def test_write_to_csv(self):
            """Test writing data to CSV"""
            mock_data = [
                [1, 'Restaurant 1', 'USA', 'New York', 'photo1.jpg', 'Event 1', '2019-03-01', '2019-03-31'],
                [2, 'Restaurant 2', 'USA', 'New York', 'photo2.jpg', 'Event 2', '2019-04-01', '2019-04-30']
            ]

            output_file = 'test_output.csv'
            write_to_csv(output_file, mock_data)
            
            with open(output_file, 'r') as file:
                lines = file.readlines()
                header = lines[0].strip()
                data = [line.strip() for line in lines[1:]]
            
            self.assertEqual(header, 'Event Id,Restaurant Id,Restaurant Name,Photo URL,Event Title,Event Start Date,Event End Date')
            self.assertEqual(data, ['1,Restaurant 1,USA,New York,photo1.jpg,Event 1,2019-03-01,2019-03-31', '2,Restaurant 2,USA,New York,photo2.jpg,Event 2,2019-04-01,2019-04-30'])
            os.remove(output_file)

if __name__ == '__main__':
    unittest.main()