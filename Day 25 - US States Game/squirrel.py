import pandas as pd

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(df.shape)
# print(df.describe())
# print(df.info)
# print(df.columns)

# print(df[df['Primary Fur Color']] == 'Gray')
fur_color = df['Primary Fur Color'].dropna().unique()
new_df = df['Primary Fur Color'].dropna()
print(fur_color)

# data_dict = {
#     'fur_color' : fur_color
# }
# dict_color = {}
print(new_df)
color_count = []
for color in fur_color:
    print(new_df[new_df == color].count())
    color_count.append(new_df[new_df == color].count())

fur_dict = {
    'Fur Color': fur_color,
    'Count': color_count
}

fur_df = pd.DataFrame(fur_dict)
fur_df.to_csv('squirrel_count.csv')



