<h2 align="center"><strong>User Documentation</strong></h2>

The developed python is a program designed to test users with their algebra linear equation abilities. The program consists of 5 different questions. The style of questions the user will be tested is questions that have a coefficient integer multiplied by a unknown number for example 2 * X = 10 and addition solving equation question for example 7 + X = 10. The user will be required to enter the number to solve the equation. The program provides the user with immediate feedback on whether the input is correct. 

### How To Launch The Program

Download the ZIP file from https://github.com/MohamedGalis/Algebra-Simple-Equation-Program.git

![Image](https://github.com/user-attachments/assets/699c5e50-4cbd-4f5c-a57b-7f4cbc65cf7d)

### Windows Steps To Run The Program

1.Extract the folder: Right-click the downloaded ZIP file and select Extract. Save and copy the file path location

   ![Image](https://github.com/user-attachments/assets/7296a173-2c7e-4cb4-ae76-03cff6b86a5d)

2.Ensure you have the Python 3.9+ installed. You can install python using this link https://www.python.org/downloads/ .

3.Search Command prompt in the search bar 

![image](https://github.com/user-attachments/assets/03be4173-ec9d-4fca-930c-977fa5fac187)

4.To access the folder's location, use the cd command to change to the desired directory. Type cd and paste file path C:\Work Categories\Apprenticeship\Northeastern University\Intensive Foundations of Computer Science\Algebra-Simple-Equation-Program-main (1)\Algebra-Simple-Equation-Program-main

![image](https://github.com/user-attachments/assets/d028cacb-6d60-4e4f-bc61-5f46dea1f11f)

5.You can now open the python script by entering the following. 

python "Simple Algebra Equation Test.py" 

![image](https://github.com/user-attachments/assets/6e3422d2-f7d2-4123-a13f-a94b4996e88e)

### Mac Steps to Run The Program

1.Ensure you have the Python 3.9+ installed. You can install python using this link https://www.python.org/downloads/ . 

2.Download the ZIP file.Open Terminal and navigate to Downloads Directory by typing cd ~/Downloads 

![image](https://github.com/user-attachments/assets/1f17cad7-c900-4fa6-92f8-4ff0ca482b09)

3.Unzip the folder by entering the following command 

 unzip -o Algebra-Simple-Equation-Program-main.zip 

(Press 'A' when it asks to replace files) 

![image](https://github.com/user-attachments/assets/c6f39d9c-4d15-4c4c-9d6a-3736a890c1f2)

4.Enter the project folder by entering cd Algebra-Simple-Equation-Program-main/ 

![image](https://github.com/user-attachments/assets/b7c2f6e6-e4cb-46dc-bd73-ba1a14fc953e)

5.Run the program python3 Simple_Algebra_Equation_Test.py 

![image](https://github.com/user-attachments/assets/2984f69d-cfbf-4a85-9f41-3d96823c651a)

6.That’s it. You can now begin to answer the questions  

![image](https://github.com/user-attachments/assets/60aa9c00-6e9f-47ff-9180-09e507302727)

### Completing The Test

The program will start by asking you for your name. It will prompt you to answer 5 Algebraic equations. Enter your answers as whole number. If your answer is correct, you will receive positive feedback, if not the program will display the correct answer. Lastly if you enter a text the program will ask you to enter a valid input as your answers need to be a whole number. At the end of the program, you will receive your final score out of 5. Good Luck! 

### Example Program Outcome 

![image](https://github.com/user-attachments/assets/97bd3f38-3345-48ab-bb17-07945f22c10c)

<h2 align="center"><strong>Technical Documentation</strong></h2>

### Welcoming User & Initial Setup 

![image](https://github.com/user-attachments/assets/2d620d03-be1e-460a-963f-ff09f2fbfdf7)

print("Welcome To The Algebra Equation Test") 

Displays a welcome message. 

name = input("Enter your name: ") 

I created a variable “name=input()” which will prompt the user to enter their name. 

print(f"Welcome, {name}! Let's test your algebra skills today.\n") 

Uses an f-string to personalize the welcome message. It takes the input of the user's name and substitute that into the print string 

print("Solve for x in each equation. You Got This! \n") 

Lastly the last print function lets the user know to ‘Solve for x in each line’ and i added \n which will create a new line for the next set of codes. 

### Defining Equations

![image](https://github.com/user-attachments/assets/b36ef6e2-f421-4aa9-a208-7ec9afadee73)

Import Random 

i imported the Random module which is a library which is used to generate random numbers. I required to import this module to create the two defined function make_a_equation1 and make_a_equation2. 

make_a_equation1() 

Generates a multiplication equation in the form: y * x = a 

Uses random.randint(-5, 10) to pick random integers for y and x. 

Returns: 

The equation string (f"{y} * x = {a}") 

The correct answer (x) 

make_a_equation2() 

Generates an addition equation in the form: d + x = g 

Uses random.randint(-5, 10) for d and x. 

Returns: 

The equation string (f"{d} + x = {g}") 

The correct answer (x) 

For each defined function i made sure it returns the equation string which is (‘{y} * x = {g}) and return the answer (‘x’). As both return functions are in f strings for each question it will generate a different equation with different numbers. 

### Creating User Input Function 

![image](https://github.com/user-attachments/assets/fc8eace6-2d86-40d0-a897-238499e8fd57)

The function get_user_guess(equation) ensures the user provides a valid integer answer. 

I created a function that asks the user to solve the equation using 

 int(input (f"Solve for x: {equation}\nYour answer: ")) 

 For this function, I used a while True loop to create an infinite loop. Below this, I added a try block, which ensures the user inputs a valid integer. If they enter text or a float, it raises an error. That’s where the except block comes in it catches the error and returns to the original try command, prompting the user again until the correct input is entered. 

### Quiz Execution 

![image](https://github.com/user-attachments/assets/dc407515-4792-4b6e-8644-88942026c83e)



























