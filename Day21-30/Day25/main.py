# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1].strip() != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict() # convert the DataFrame to a dictionary
# print(data_dict)

temp_list = data["temp"].to_list() # convert the DataFrame to a list
print(temp_list)

# def average(list):
#     return sum(list) / len(list)

# print(average(temp_list))

print(data["temp"].mean()) # calculate the mean of the temperature