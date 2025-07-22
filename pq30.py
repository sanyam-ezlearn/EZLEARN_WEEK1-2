'''How to create filename containing date or time in Python'''
# import module
from datetime import datetime

# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print("Current date & time : ", current_datetime)

# convert datetime obj to string
str_current_datetime = str(current_datetime)

# create a file object along with extension
file_name = str_current_datetime+".txt"
file = open(file_name, 'w')

print("File created : ", file.name)
file.close()
