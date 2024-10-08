import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
file_path = 'your_file.csv'  # Replace 'your_file.csv' with your actual file path
df = pd.read_csv(file_path)

# Plot the data
plt.plot(df['x_column'], df['y_column'])  # Replace 'x_column' and 'y_column' with the actual column names
plt.xlabel('X-axis label')  # Customize the x-axis label
plt.ylabel('Y-axis label')  # Customize the y-axis label
plt.title('Plot Title')  # Customize the plot title
plt.show()
