#!/bin/bash

# Set the input and output file paths
input_file="ips.txt"
output_file="latency.txt"

# Loop through each IP address in the input file
while read ip; do

  # Send a GET request to the IP address using telnet and measure the response time
  start_time=$(date +%s.%N)
  (echo "GET / HTTP/1.1\n\n" | telnet $ip 8080 > /dev/null)
  end_time=$(date +%s.%N)
  response_time=$(echo "$end_time - $start_time" | bc)

  # Write the IP address and response time to the output file
  echo "$ip,$response_time" >> $output_file

done < $input_file

