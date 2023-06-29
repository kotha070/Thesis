import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel('ping_rtt_stats.xlsx')

# Extract the data from the desired column
column_data = df['Mdev'].dropna()

# Calculate the PDF using numpy
values, base = np.histogram(column_data, bins=40, density=True)
cumulative = np.cumsum(values * np.diff(base))

# Plotting the PDF graph
plt.plot(base[:-1], values)
plt.xlabel('Data')
plt.ylabel('Probability Density')
plt.title('PDF of Data')
plt.grid(True)
plt.show()
