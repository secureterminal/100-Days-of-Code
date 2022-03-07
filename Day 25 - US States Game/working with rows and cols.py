# with open('weather_data.csv') as data:
#     data = data.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data:
#     data = csv.reader(data)
#     temperatures = []
#     count = 0
#     for row in data:
#         print(row)  # prints each row as a list
#         if count > 0:
#             temperatures.append(int(row[1]))
#         count += 1
#     print(temperatures)

import pandas

df = pandas.read_csv('weather_data.csv')
print(df)
print(type(df))
print(type(df['temp']))
print(df['temp'])

data_dict = df.to_dict()
print(data_dict)

temp_list = df['temp'].to_list()
print(temp_list)
average = sum(temp_list)/len(temp_list)
print(average)

print(df['temp'].mean())
print(df['temp'].max())


# Get data in columns
print(df.condition)


# Get Data in rows
print(df[df.day == 'Monday'])
print(df[df.temp == df.temp.max()])
print(df[df.temp == df.temp.max()]['condition'])
monday = df[df.day == 'Monday']
print((monday.temp * 1.8) + 32)

# create a df from dict

data_dict = {
    'students': ['Amy', 'James', 'Sandra'],
    'scores': [12, 55, 90]
}

df = pandas.DataFrame(data_dict)
df.to_csv('new_data.csv')
