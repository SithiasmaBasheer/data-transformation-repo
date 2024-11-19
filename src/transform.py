import os
import json

# Function to transform the data
def transform_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                try:
                    record = json.loads(line.strip())
                    # Remove PII fields
                    record.pop("C_FIRST_NAME", None)
                    record.pop("C_LAST_NAME", None)
                    # Transform C_EMAIL_ADDRESS to C_EMAIL_DOMAIN
                    if "C_EMAIL_ADDRESS" in record:
                        email = record.pop("C_EMAIL_ADDRESS")
                        record["C_EMAIL_DOMAIN"] = email.split('@')[-1] if '@' in email else None
                    # Write the transformed record to the output file
                    outfile.write(json.dumps(record) + '\n')
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}. Skipping line: {line.strip()}")
                except Exception as e:
                    print(f"Unexpected error processing line: {line.strip()} - {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    try:
        # Input and output paths
        input_dir = "data-exports/TPCDS_SF10TCL/customer/"
        output_dir = "data-exports/TPCDS_SF10TCL/transformed/"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # To automate the transformation for all files in the directory
        for file_name in os.listdir(input_dir):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, file_name.replace('.txt', '_transformed.txt'))
            if os.path.isfile(input_file): # Ensure it's a file, not a directory
                print(f"Processing file: {file_name}")
                transform_data(input_file, output_file)
                print(f"Successfully transformed: {file_name}")
    except FileNotFoundError as e:
        print(f"Input directory not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred in the main function: {e}")


if __name__ == '__main__':
    main()