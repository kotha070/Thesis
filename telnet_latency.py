import telnetlib
import time

# File paths
input_file = "ips.txt"
output_file = "telenet_latency_results.txt"

def measure_latency(ip):
    try:
        # Connect to the IP address on port 8080
        start_time = time.time()
        tn = telnetlib.Telnet(ip, 8080)
        end_time = time.time()
        tn.close()

        # Calculate the latency time in milliseconds
        latency = (end_time - start_time) * 1000
        return latency
    except Exception as e:
        print(f"Error measuring latency for {ip}: {str(e)}")
        return None

def main():
    # Read IP addresses from input file
    with open(input_file, "r") as file:
        ip_addresses = file.read().splitlines()

    # Measure latency for each IP address
    latency_results = []
    for ip in ip_addresses:
        latency = measure_latency(ip)
        if latency is not None:
            latency_results.append((ip, latency))

    # Save latency results to output file
    with open(output_file, "w") as file:
        for ip, latency in latency_results:
            file.write(f"{ip}: {latency} ms\n")

    print("Latency measurement complete.")

if __name__ == "__main__":
    main()

