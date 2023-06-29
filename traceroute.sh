#!/bin/bash

# Input file containing the IP addresses
input_file="ips.txt"

# Output file to store the traceroute results
output_file="traceroute_results_dup.txt"

# Remove the output file if it already exists
if [ -f $output_file ]; then
  rm $output_file
fi

# Loop through each IP address in the input file
while read ip_address; do
  echo "Running traceroute for IP address: $ip_address"

  # Run the traceroute command and store the output in the output file
  traceroute "$ip_address" >> $output_file

  # Add a separator between the output of each traceroute command
  echo "-----------------------------------" >> $output_file
done < $input_file

