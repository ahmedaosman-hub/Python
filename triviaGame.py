# Trivia Game
# Objective: Ask user 5 questions and display the 5 possible answers. Ensures user does not input something other than A, B, C or D.
#   Displays correct answers and displays overall score.
# Created on 11/23/2022 by Ahmed Osman

# Questions to display
questions = ("How long is an Olympic swimming pool (in meters)?: ",
             "What does 'www' stand for in a website browser?:",
             "Who named the Pacific Ocean?:",
             "Which animal is on the Porsche Logo?:",
             "What is the largest ocean on earth?: ")

# Possible options of answer
options = (("A. 100", "B. 50", "C. 1 ", "D. 65"),
           ("A. World Web Wide", "B. World Wode Web", "C. World Wide Web", "D. World Wade Web"),
           ("A. Ferdinand Magellan", "B. Albert Einstein", "C. Ahmed Osman", "D. Barack Obama"),
           ("A. Snail", "B. Shrimp", "C. Horse", "D. Unicorn"),
           ("A. Atlantic Ocean ", "B. Pacific Ocean ", "C. Gulf of Mexico", "D. Indian Ocean "))

# Correct answers
answers = ("B", "C", "A", "C", "B")

# Initializes these variables
guesses = []
score = 0
question_number = 0

# For each question in the array questions, print a broken line and question.
for question in questions:
    print("-------------------------")
    print(question)
    # For each option in the array options, display the options according to the question you are on. Then print that option
    for option in options[question_number]:
        print(option)

    # Allows user input of different options
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    # Ensures user inputs an answer that is A,B,C, or D
    while guess != ("A") and guess != ("B") and guess != ("C") and guess != ("D"):
        print("Incorrect Response. Please enter (A, B, C, D):")
        guess = input("Enter (A, B, C, D): ").upper()
    # If the inputted answer is the correct answer. Increase their score and print a message.
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
        # Was unable to have this function move onto the next question without this.
        question_number += 1
    else:
        print("Incorrect!")
        print(f"{answers[question_number]} is the correct answer")
        # Was unable to have this function move onto the next question without this
        question_number += 1

print("-------------------------")
print("        Results          ")
print("-------------------------")



#Show the correct answers after this
print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

#Show the user their inputted answers
print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()


#Calculates the users score
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
