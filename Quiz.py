# Dictionary that stores questions and answers
quiz = {
    "Question_1": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "Question_2": {
        "question": "What is the capital of Costa Rica?",
        "answer": "San Jose" 
    },
    "Question_3": {
        "question": "What is the capital of Mexico?",
        "answer": "Mexico City"
    },
    "Question_4": {
        "question": "What is the capital of Brazil?",
        "answer": "Brasilia"
    },
    "Question_5": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "Question_6": {
        "question": "What is the capital of Texas?",
        "answer": "Austin"
    }
}

# Have a variable that tracks player score
score = 0

# Loop through the dictionary using the key value pairs
for key, value in quiz.items():
    # Display each question to the user and allow them to answer
    print(value['question'])
    answer = input("What is the answer? ")

    # Tell them if they are right or wrong
    if answer.lower() == value['answer'].lower():
        print("That's correct!")
        score = score + 1
        print(f"Your score is: {score}")
        print("")
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print(f"Your score is: {score}")
        print("")

# Show the final result when quiz is completed
print(f"Your final score is: {score} out of 6 questions correct")
print("Percentage correct: " + str(int(score/6 * 100)) + "%")