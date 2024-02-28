import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
data = np.loadtxt("your_csv_file.csv", delimiter=",")

# Assuming the CSV file has two columns for x and y coordinates
x_values = data[:, 0]
y_values = data[:, 1]

# Create contour map
plt.figure(figsize=(8, 6))
contour_plot = plt.contourf(x_values, y_values, cmap='viridis')
plt.colorbar(contour_plot, label='Density')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Contour Map from CSV Data')
plt.show()
