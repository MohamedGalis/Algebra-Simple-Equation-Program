# Print Function to Welcome the User

print("Welcome To The Algebra Equation Test")
name = input("Enter your name: ")
print(f"Welcome, {name}! Let's test your algebra skills today.\n")
print("Solve for x in each equation. You Got This! \n")

# Need to import 'Random Module' so i can generate numbers for the 2 different types of equation created
import random

def make_a_equation1():
    """Generates a multiplication equation in the form of y * x = a and returns the equation string and correct answer."""
    y = random.randint(-5, 10)  # Avoid 0 to ensure solvability
    x = random.randint(-5, 10)
    a = y * x
    return (f"{y} * x = {a}", x)  # Returns equation and answer. Will use this later on to checks users answer

def make_a_equation2():
    """Generates an addition equation in the form of d + x = g and returns the equation string and correct answer."""
    d = random.randint(-5, 10)  # Numbers between -5 to 15
    x = random.randint(-5, 10)
    g = d + x
    return (f"{d} + x = {g}", x)

# Function to display the type of equation
def get_user_guess(equation):
    while True:
        try:
            return int(input(f"Solve for x: {equation}\nYour answer: ")) # Users response need to be a integer and String for the equation
        except ValueError:
            print("Incorrect input! Please enter a valid number.") # If user inputs text. It will display the following until they enter a integer

# Score starts a 0 and 5 Questions will generated
score = 0  
test_questions = 5 

# Runs the quiz 5 times
for i in range(test_questions):
    equation_type = random.choice([1, 2])
    
    if equation_type == 1:
        equation, correct_answer = make_a_equation1()  
    else:
        equation, correct_answer = make_a_equation2()

    user_answer = get_user_guess(equation)  

    if user_answer == correct_answer: 
        print("✅Correct!\n") 
        score += 1  
    else: 
        print(f"❌Wrong! The correct answer was {correct_answer}.\n")

# Prints final score and thanks the user for completing the test 
print(f"Test Over! You scored {score} out of {test_questions}.") 
print("Thanks for completing the Algebra Test")