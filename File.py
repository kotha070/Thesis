import csv
import json

# Path to your input and output files
input_file = 'output.txt'
output_file = 'output.csv'

# Read the JSON data from the input file
with open(input_file, 'r') as file:
    json_data = file.readlines()

# Convert each JSON record to a Python dictionary
data = [json.loads(record.strip()) for record in json_data]

# Extract the field names from the first record
field_names = list(data[0].keys())

# Write the data to a CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

print(f"Output saved to {output_file}")

