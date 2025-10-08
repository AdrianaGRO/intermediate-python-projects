import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}



response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()


# data["results"] is a list of question dictionaries
question_data = data["results"]
print(question_data)

# Extract correct answers from each question dictionary
correct_answers = [item["correct_answer"] for item in question_data]
print("Correct answers:", correct_answers)

# Extract questions from each question dictionary
questions = [item["question"] for item in question_data]
print("Questions:", questions)