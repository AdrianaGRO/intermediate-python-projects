import pandas as pd

# 1. Read the squirrel data
data = pd.read_csv("24_Central_Park_Squirrel_Census/2018_Central_Park_Squirrel_Census_20250911.csv")

# 2. Count the number of squirrels of each color
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(f"Number of gray squirrels: {len(gray_squirrels)}")
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
print(f"Number of red squirrels: {len(red_squirrels)}")
black_squirrels = data[data["Primary Fur Color"] == "Black"]
print(f"Number of black squirrels: {len(black_squirrels)}")

# 3. Create a summary DataFrame
squirrel_counts = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
}   
summary_df = pd.DataFrame(squirrel_counts)
print(summary_df)

# 4. Save the DataFrame to a CSV file without the index column
summary_df.to_csv("24_Central_Park_Squirrel_Census/squirrel_count.csv", index=False)
