import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel('ping_rtt_stats.xlsx')

# Extract data from the DataFrame column
data = df['Min'].dropna().tolist()

# Calculate the CDF using numpy
values, base = np.histogram(data, bins=40, density=True)
cumulative = np.cumsum(values * np.diff(base))

# Plotting the CDF graph
plt.plot(base[:-1], cumulative)
plt.xlabel('Data')
plt.ylabel('Cumulative Probability')
plt.title('CDF of Data')
plt.grid(True)
plt.show()

