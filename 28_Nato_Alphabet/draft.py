# numbers = [1,2,3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# PyDev console: starting.
# Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]
# print(new_list)
# [2, 3, 4]
# name = [ "Adriana"]
# new_list = [letter for letter in name]
# print(new_list)
# ['Adriana']
# new_list = [letter + letter for letter in name]
# print(new_list)
# ['AdrianaAdriana']
# letter_lists = [ letter for letter in name]
# name = "Adriana"
# new_list = [ letter for letter in name]
# print(name)
# Adriana
# print(new_list)
# ['A', 'd', 'r', 'i', 'a', 'n', 'a']
# range(1,6)
# range(1, 6)
# list = (n * n for n in range(1,6))
# print(list)
# <generator object <genexpr> at 0x1054553c0>
# list = [n * n for n in range(1,6)]
# print(list)
# [1, 4, 9, 16, 25]
# names = [ "Alex", "Beth", "Caroline", "Davve", "Eleonor", "Felipe"]
# my_list = [name for name in names if len(name) < 5]
# print(my_list)
# ['Alex', 'Beth', 'Dave']
# upper_case = [name.upper() for name in names if len(name) > 5 ]
# print(upper_case)
# ['CAROLINE', 'ELEANOR', 'FELIPE']


# Filtering Even Numbers
# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.   

# First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   
# Then use list comprehension again to create a new list called result.
# This new list should only contain the even numbers from the list numbers. 
# Again, try to use Python's List Comprehension instead of a Loop. 

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(number) for number in list_of_strings ]
# print(numbers)
#
# result = [number for number in numbers if number % 2 == 0 ]
# print(result)

#Data Overlap
# 💪 This exercise is HARD 💪 
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
# You are going to create a list called result which contains the numbers that are common in both files. 
# e.g. if file1.txt contained: 
# 1 
# 2 
# 3
# and file2.txt contained: 
# 2
# 3
# 4
# result = [2, 3]

# IMPORTANT:  The output should be a list of integers and not strings!
# Try to use List Comprehension instead of a Loop. 

# with open("/Users/adricati/Personal Development/intermediate-python-projects/28_Nato_Alphabet/file1.txt", "r") as file1:
#     numbers_file_one = [line.strip() for line in file1.readlines()]


# print(numbers_file_one)

# with open("/Users/adricati/Personal Development/intermediate-python-projects/28_Nato_Alphabet/file2.txt", "r") as file2:
#     numbers_file_two = [line.strip() for line in file2.readlines()]

# print(numbers_file_two)


# common = [int(number) for number in numbers_file_one if number in numbers_file_two ]
# print(common)

#Dictionary Comprehension
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each
# word in the list and makes it the key and the value is how many letters are in the word.
# e.g. { "word": 4 }
# words = ['apple', 'banana', 'cherry', 'date']
# result = {word: len(word) for word in words}
# print(result)
# {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}
# import random
# names = [ "Alex", "Beth", "Caroline", "Davve", "Eleonor", "Felipe"]
# students_scores = {student:random.randint(30,100) for student in names}
# passed_students = {student:score for (student, score) in students_scores.items() if int(score) > 90}

# Dictionary Comprehension 1
# You are going to use Dictionary Comprehension to create a dictionary called result that
# takes each word in the given sentence and calculates the number of letters in each word.   
# Try Googling to find out how to convert a sentence into a list of words.  *
# *Do NOT** Create a dictionary directly.
# Try to use Dictionary Comprehension instead of a Loop. 

# To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)


# Dictionary Comprehension 2
# You are going to use Dictionary Comprehension to create a dictionary called weather_f
# that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 

# To convert temp_c into temp_f use this formula: 
# (temp_c * 9/5) + 32 = temp_f

# Celsius to Fahrenheit chart

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21,
#              "Saturday": 22, "Sunday": 24}
#
# weather_f = {day: (temp_c *9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}   


for (key, value) in student_dict.items():
    print(key)
    print(value)
    
    
import pandas as pd

student_data_frame = pd.DataFrame(student_dict, index=["a", "b", "c"])
print(student_data_frame)

# #Loop through rows of a data frame
# for (key, value) in student_data_frame.items():
    
#     print(value)

#Loo[p through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)