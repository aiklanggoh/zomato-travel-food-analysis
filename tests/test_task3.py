import unittest
import json
import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task3 import load_json_file, determine_rating_thresholds


class TestTask3(unittest.TestCase):
    
    def test_load_json_file(self):
        """Test loading JSON file"""
        test_data = [{'key': 'value'}]
        with open('test_data.json', 'w') as file:
            json.dump(test_data, file)
        
        result = load_json_file('test_data.json')
        self.assertEqual(result, test_data)

        os.remove('test_data.json')

    def test_determine_rating_thresholds(self):
        """Test determining rating thresholds"""
        test_data = [
            {
                "restaurants": [
                    {
                        "restaurant": {
                            "user_rating": {
                                "aggregate_rating": "4.5",
                                "rating_text": "Excellent"
                            }
                        }
                    },
                    {
                        "restaurant": {
                            "user_rating": {
                                "aggregate_rating": "3.5",
                                "rating_text": "Very Good"
                            }
                        }
                    },
                    {
                        "restaurant": {
                            "user_rating": {
                                "aggregate_rating": "2.5",
                                "rating_text": "Good"
                            }
                        }
                    },
                    {
                        "restaurant": {
                            "user_rating": {
                                "aggregate_rating": "1.5",
                                "rating_text": "Average"
                            }
                        }
                    },
                    {
                        "restaurant": {
                            "user_rating": {
                                "aggregate_rating": "0.5",
                                "rating_text": "Poor"
                            }
                        }
                    }
                ]
            }
        ]
        result = determine_rating_thresholds(test_data)
        expected = {
            "Excellent": {
                "min": 4.5,
                "max": 4.5,
                "count": 1,
                "average": 4.5
            },
            "Very Good": {
                "min": 3.5,
                "max": 3.5,
                "count": 1,
                "average": 3.5
            },
            "Good": {
                "min": 2.5,
                "max": 2.5,
                "count": 1,
                "average": 2.5
            },
            "Average": {
                "min": 1.5,
                "max": 1.5,
                "count": 1,
                "average": 1.5
            },
            "Poor": {
                "min": 0.5,
                "max": 0.5,
                "count": 1,
                "average": 0.5
            }
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()