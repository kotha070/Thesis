import subprocess

input_file = "ips.txt"
output_file = "ping_results.txt"

# Open the input file and read IP addresses
with open(input_file, "r") as file:
    ip_addresses = file.read().splitlines()

# Open the output file to write the results
with open(output_file, "w") as file:
    # Loop through each IP address
    for ip_address in ip_addresses:
        # Run the ping command and capture the output
        ping_process = subprocess.Popen(["ping", "-n", "4", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = ping_process.communicate()

        # Write the IP address and ping output to the output file
        file.write(f"IP Address: {ip_address}\n")
        file.write(output)
        file.write("\n")

# Print a success message
print("Ping results recorded successfully!")

