
import csv
import pandas as pd

# with open("23_CSV_files_PANDAS/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#     for line in data:
#         print(line.strip())
#         print(line.split(","))
        
    
# with open("23_CSV_files_PANDAS/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # Enumerate gives you the index and the value
#     for i, row in enumerate(data): # Iterate through the rows enumerated 
#         print(row)
#         if i > 0: #skip the header row
#             temperatures.append(float(row[1]))

#     print(temperatures)
    
    
data = pd.read_csv("23_CSV_files_PANDAS/weather_data.csv")
# print(type(data))
# print(data)
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)
print(data["temp"].to_list())
print(len(data["temp"].to_list()))


# Statistical methods in pandas:
# .mean() - Calculates the average value (sum of all values divided by count)
print(data["temp"].mean())

# .max() - Returns the highest value in the dataset
print(data["temp"].max())   

# .min() - Returns the lowest value in the dataset
print(data["temp"].min())

# Additional useful statistical methods:
# .median() - Middle value when data is sorted (better than mean for skewed data)
print(f"Median temperature: {data['temp'].median()}")

# .std() - Standard deviation (measures how spread out the data is from the mean)
# A low standard deviation means most values are close to the average
# A high standard deviation means values are more spread out
# Example: std of [10,10,10,10] is 0 (no variation)
#          std of [5,10,15,20] is 6.45 (high variation)
print(f"Standard deviation: {data['temp'].std()}")

# To visualize: approximately 68% of values fall within 1 std deviation of the mean
# and 95% fall within 2 std deviations
low_range = data['temp'].mean() - data['temp'].std()
high_range = data['temp'].mean() + data['temp'].std()
print(f"68% of temperatures are likely between {low_range:.2f} and {high_range:.2f}")

# .describe() - Generates summary statistics for numerical data
print("\nSummary statistics:")
print(data["temp"].describe())

# .value_counts() - Counts unique values (useful for categorical data)
print("\nWeather condition counts:")
print(data["condition"].value_counts())

print(data.condition)



#get data in a row
print("\nData for Monday:")
print(data[data.day == "Monday"])

#get data in a row where temp is max
print("\nData for the day with highest temperature:")
print(data[data.temp == data.temp.max()])

# get the particular temperature on a specific day
monday = data[data.day == "Monday"]
monday_condition = monday.condition
monday_temp = int(monday.temp) * 9/5 + 32
print(f"\nMonday's condition: {monday_condition}, Temperature in Fahrenheit: {monday_temp}")

#create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
print("\nDataFrame from scratch:")
print(data)
data.to_csv("23_CSV_files_PANDAS/new_data.csv", index=False) # Save to CSV without the index column