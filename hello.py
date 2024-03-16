
import psutil
# gives a single float value
print('The CPU usage is: ', psutil.cpu_percent(1))

# gives an object with many fields
psutil.virtual_memory()
# you can convert that object to a dictionary 
dict(psutil.virtual_memory()._asdict())
# you can have the percentage of used RAM
psutil.virtual_memory().percent
#79.2
# you can calculate percentage of available memory
print('available memory', psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
