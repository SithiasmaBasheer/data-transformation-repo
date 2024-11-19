import unittest
import json
import os
from src import transform_data


class TestDataTransformation(unittest.TestCase):
    
    def setUp(self):
        """Set up sample input and output files for testing."""
        self.input_file = "test_input.jsonl"    # JSONL is same as JSON format but implemented using newline characters to separate JSON values.
        self.output_file = "test_output.jsonl"
        
        self.sample_data = [
            {
                "C_CUSTOMER_ID": "1",
                "C_FIRST_NAME": "John",
                "C_LAST_NAME": "Doe",
                "C_EMAIL_ADDRESS": "john.doe@example.com",
                "C_BIRTH_COUNTRY": "USA"
            },
            {
                "C_CUSTOMER_ID": "2",
                "C_FIRST_NAME": "Jane",
                "C_LAST_NAME": "Smith",
                "C_EMAIL_ADDRESS": "jane.smith@domain.org",
                "C_BIRTH_COUNTRY": "UK"
            }
        ]
        with open(self.input_file, 'w') as f:
            for record in self.sample_data:
                f.write(json.dumps(record) + '\n')

    def tearDown(self):
        """Clean up the files after tests."""
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_transformation(self):
        """Test the data transformation function."""
        transform_data(self.input_file, self.output_file)
        
        # Read the transformed data
        with open(self.output_file, 'r') as f:
            transformed_data = [json.loads(line.strip()) for line in f]
        
        # Validate the transformations
        self.assertEqual(len(transformed_data), len(self.sample_data))  # Same number of records
        
        # Check first record
        self.assertNotIn("C_FIRST_NAME", transformed_data[0])
        self.assertNotIn("C_LAST_NAME", transformed_data[0])
        self.assertNotIn("C_EMAIL_ADDRESS", transformed_data[0])
        self.assertIn("C_EMAIL_DOMAIN", transformed_data[0])
        self.assertEqual(transformed_data[0]["C_EMAIL_DOMAIN"], "example.com")
        
        # Check second record
        self.assertNotIn("C_FIRST_NAME", transformed_data[1])
        self.assertNotIn("C_LAST_NAME", transformed_data[1])
        self.assertNotIn("C_EMAIL_ADDRESS", transformed_data[1])
        self.assertIn("C_EMAIL_DOMAIN", transformed_data[1])
        self.assertEqual(transformed_data[1]["C_EMAIL_DOMAIN"], "domain.org")

if __name__ == "__main__":
    unittest.main()
