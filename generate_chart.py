import matplotlib.pyplot as plt
import psutil

# Sample data
#x = [1, 2, 3, 4, 5]
#y = [2, 3, 5, 7, 11]

# Plotting the data
#plt.plot(x, y)
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.title('Sample Chart')
#plt.grid(True)

# Save the chart as an image
#plt.savefig('sample_chart.png')

# Show the chart
# plt.show()

x=[0]
y= [0]
z=[1]
count = 1
while (count < 20):
  count=count+1 
  z.append(count)
  # gives a single float value
  x.append(psutil.cpu_percent(1))
 # print('The CPU usage is: ', psutil.cpu_percent(1))
  
  # gives an object with many fields
  psutil.virtual_memory()
  # you can convert that object to a dictionary 
  dict(psutil.virtual_memory()._asdict())
  # you can have the percentage of used RAM
  psutil.virtual_memory().percent
  #79.2
  y.append(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
  # you can calculate percentage of available memory
 # print('available memory', psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

plt.plot(z, x)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Chart')
plt.grid(True)
plt.savefig('cpu_chart.png')
plt(z,y)
plt.savefig('memory_chart.png')

