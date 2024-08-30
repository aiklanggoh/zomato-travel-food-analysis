import unittest
import json
import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task1 import load_json_file, load_country_codes, extract_restaurant_data, write_to_csv

class TestTask1(unittest.TestCase):
    def test_load_json_file(self):
        """Test loading JSON file"""
        test_data = [{'key': 'value'}]
        with open('test_data.json', 'w') as file:
            json.dump(test_data, file)
        
        result = load_json_file('test_data.json')
        self.assertEqual(result, test_data)

        os.remove('test_data.json')
    
    def test_load_country_code(self):
        """Test loading country codes"""
        mock_data = {
            '1': 'USA',
            '14': 'Canada'
        }
        mock_df = pd.DataFrame({
            'Country Code': ['1', '14'],
            'Country': ['USA', 'Canada']
        })
        mock_df.to_excel('test_country_codes.xlsx', index=False)
        mock_read_excel = pd.read_excel('test_country_codes.xlsx', dtype={'Country Code': str})
        mock_dict = mock_read_excel.set_index('Country Code')['Country'].to_dict()
        self.assertEqual(mock_dict, mock_data)

        os.remove('test_country_codes.xlsx')


    def test_extract_restaurant_data(self):
        """Test extracting restaurant data"""
        mock_data = [
            {
                'restaurants': [
                    {
                        'restaurant': {
                            'id': 1,
                            'name': 'Restaurant 1',
                            'location': {
                                'country_id': '1',
                                'city': 'New York'
                            },
                            'user_rating': {
                                'votes': 100,
                                'aggregate_rating': '4.5'
                            },
                            'cuisines': 'Italian'
                        }
                    }
                ]
            }
        ]
        mock_country_codes = {
            '1': 'USA'
        }
        result = extract_restaurant_data(mock_data, mock_country_codes)
        expected = [
            [1, 'Restaurant 1', 'USA', 'New York', 100, 4.5, 'Italian']
        ]
        self.assertEqual(result, expected)

    def test_write_to_csv(self):
        """Test writing data to CSV"""
        mock_data = [
            [1, 'Restaurant 1', 'USA', 'New York', 100, 4.5, 'Italian']
        ]
        output_file = 'test_output.csv'
        write_to_csv(output_file, mock_data)
        
        with open(output_file, 'r') as file:
            lines = file.readlines()
            header = lines[0].strip()
            data = [line.strip() for line in lines[1:]]
        
        self.assertEqual(header, 'Restaurant Id,Restaurant Name,Country,City,User Rating Votes,User Aggregate Rating,Cuisines')
        self.assertEqual(data, ['1,Restaurant 1,USA,New York,100,4.5,Italian'])

        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()