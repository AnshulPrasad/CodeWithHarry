import random
import requests


# fetch questions and answers using Open Trivia DB API
parameters = {
    "amount": 20,  # number of questions
    "type": "multiple",  # type of questions
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]


# fill the lists with question and answers(correct+incorrect)
questions = []
correct_answer = []
incorrect_answers = []

for i in question_data:
    questions.append(i["question"])
    correct_answer.append(i["correct_answer"])
    incorrect_answers.append(i["incorrect_answers"])


# Quiz
print("Quiz\nTotal 10 questions\nEarn 1 point per question\n1 point = Rs 5000")

j = 1
point = 0

for i in random.sample(range(20), 10):
    # ask question
    print(f"\nQuestion {j}: {questions[i]}")

    # present options as list
    options = incorrect_answers[i] + [correct_answer[i]]
    random.shuffle(options)
    print(f"options: {options}")

    # take use input and handle error
    try:
        chosen_answer = int(input("Enter the correct option number: "))
    except:
        print("Please enter a number.\nNo points.")
        j += 1
        continue

    # check input validity
    if not 1 <= chosen_answer <= len(options):
        print("Number out of range.\nNo points.")
        j += 1
        continue

    # increase point if answer is correct
    if options[chosen_answer - 1] == correct_answer[i]:
        point += 1

    # reveal correct answer number
    print(f"correct option: {options.index(correct_answer[i])+1}")

    j += 1

# calculate the score and amount earned.
print(f"\nTotal score: {point}")
print(f"You won: Rs {point*5000}")
