# multiple choice quiz game

questions = (
    "Which keyword is used to define a function in Python?",
    "What is the output of len('Hello') in Python?",
    "Which HTTP status code indicates 'Not Found'?",
    "Which of the following is a Python immutable data type?",
    "Which SQL command is used to remove a table from a database?",
)

options = (
    ("A. func", "B. define", "C. def", "D. function"),
    ("A. 4", "B. 5", "C. Hello", "D. hello"),
    ("A. 200", "B. 301", "C. 404", "D. 500"),
    ("A. list", "B. dictionary", "C. tuple", "D. set"),
    ("A. DROP TABLE", "B. DELETE TABLE", "C. REMOVE TABLE", "D. TRUNCATE TABLE"),
)

answers = ["C", "B", "C", "C", "A"]
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("\nenter (A, B, C, D): ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("\n------------------------------------------------------------")
print("                        RESULTS                             ")
print("------------------------------------------------------------")

print(f"answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print(f"\nguesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

print(f"\nyour score is {score}")
