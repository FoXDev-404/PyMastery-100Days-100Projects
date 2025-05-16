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

# print(data["temp"].mean()) # calculate the mean of the temperature

# print(data["temp"].max()) # calculate the max of the temperature


# Get data in columns
# print(data["condition"])
# print(data.condition) # same as above

# Get data in rows
# print(data[data.day == "Monday"]) # get the row where the day is Monday
# print(data[data.temp == data.temp.max()]) # get the row where the temperature is max

# monday = data[data.day == "Monday"] # get the row where the day is Monday
# print(monday.condition) # get the condition of Monday
# print(monday.temp * 9/5 + 32) # convert the temperature to Fahrenheit


# Create a dataframe from scratch
data_dict = {
    "student": ["Raj", "Nik", "Subh"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")