import requests
import json

API_KEY = '555f4ad047c24508bef4e13cd450cfb8'  # Replace 'your_api_key' with your actual ipgeolocation.io API key
input_file = 'ips.txt'  # Path to your input file
output_file = 'output.txt'  # Path to your output file

# Function to query ipgeolocation.io for IP information
def query_ip(ip):
    url = f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}&fields=geo,timezone'  # Modify the "fields" parameter based on your desired output
    response = requests.get(url)
    return response.json()

# Read input file and process IP addresses
with open(input_file, 'r') as file:
    ip_list = file.read().splitlines()

output_data = []

# Query IP information for each IP address
for ip_address in ip_list:
    ip_info = query_ip(ip_address)
    output_data.append(ip_info)

# Write output to a new file
with open(output_file, 'w') as file:
    for ip_info in output_data:
        file.write(json.dumps(ip_info) + '\n')

print(f"Output saved to {output_file}")

