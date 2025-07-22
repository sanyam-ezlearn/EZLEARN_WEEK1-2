'''Python program to convert unix timestamp string to readable date'''
# Importing datetime module
import datetime

print(datetime.datetime.fromtimestamp(int("1294113662"))
      .strftime('%Y-%m-%d %H:%M:%S'))