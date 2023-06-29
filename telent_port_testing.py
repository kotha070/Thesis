import telnetlib

# File paths
input_file = "ips.txt"
output_file = "port_test_results.txt"
port = 8080  # Change this to the desired port number

def test_port(ip, port):
    try:
        tn = telnetlib.Telnet(ip, port, timeout=5)
        tn.close()
        return True
    except Exception as e:
        print(f"Port {port} is closed on {ip}: {str(e)}")
        return False

def main():
    # Read IP addresses from input file
    with open(input_file, "r") as file:
        ip_addresses = file.read().splitlines()

    # Test port for each IP address
    port_test_results = []
    for ip in ip_addresses:
        port_status = test_port(ip, port)
        port_test_results.append((ip, port_status))

    # Save port test results to output file
    with open(output_file, "w") as file:
        for ip, port_status in port_test_results:
            file.write(f"{ip}: {'Open' if port_status else 'Closed'}\n")

    print("Port testing complete.")

if __name__ == "__main__":
    main()

