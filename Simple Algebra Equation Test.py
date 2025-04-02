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


