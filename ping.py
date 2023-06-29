import subprocess

input_file = "ips.txt"
output_file = "ping_results.sh"

# Open the input file and read IP addresses
with open(input_file, "r") as file:
    ip_addresses = file.read().splitlines()

# Open the output file to write the ping commands
with open(output_file, "w") as file:
    # Loop through each IP address
    for ip_address in ip_addresses:
        # Create the ping command
        ping_command = f"ping -c 4 {ip_address} >> ping_output.txt\n"

        # Write the ping command to the output file
        file.write(ping_command)

# Print a success message
print("Ping commands generated successfully!")

