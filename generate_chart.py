import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plotting the data
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Chart')
plt.grid(True)

# Save the chart as an image
plt.savefig('sample_chart.png')

# Show the chart
# plt.show()
