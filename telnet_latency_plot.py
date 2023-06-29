import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel('ping_rtt_stats.xlsx')

ip_addresses = df.columns[1:]  # Assuming IP addresses are in the second column onwards
average_rtt = []
for ip_address in ip_addresses:
    ip_data = df[ip_address].dropna()  # Extract RTT data for the specific IP address
    average_rtt.append(ip_data.mean())  # Calculate the average RTT for the IP address

# Plotting PDF graph
plt.figure()
# Calculate the PDF using numpy
values, base = np.histogram(average_rtt, bins=40, density=True)
# Calculate the cumulative distribution function (CDF) using numpy
cumulative = np.cumsum(values * np.diff(base))
# Plotting the PDF graph
plt.plot(base[:-1], values)
plt.xlabel('Average RTT')
plt.ylabel('Probability Density')
plt.title('PDF of Average RTT')
plt.grid(True)
plt.show()
