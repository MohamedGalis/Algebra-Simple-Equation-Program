<h2 align="center"><strong>User Documentation</strong></h2>

The developed python is a program designed to test users with their algebra linear equation abilities. The program consists of 5 different questions. The style of questions the user will be tested is questions that have a coefficient integer multiplied by a unknown number for example 2 * X = 10 and addition solving equation question for example 7 + X = 10. The user will be required to enter the number to solve the equation. The program provides the user with immediate feedback on whether the input is correct. 

### How To Launch The Program

Download the ZIP file from

```
https://github.com/MohamedGalis/Algebra-Simple-Equation-Program.git
```

![Image](https://github.com/user-attachments/assets/699c5e50-4cbd-4f5c-a57b-7f4cbc65cf7d)

### Windows Steps To Run The Program

1.Extract the folder: Right-click the downloaded ZIP file and select Extract. Save and copy the file path location

![image](https://github.com/user-attachments/assets/1f5f9c41-8816-48fa-94c0-faa841715180)

2.Ensure you have the Python 3.13.2 installed. You can install python using this link 

```
https://www.python.org/downloads/
```

3.Search Command prompt in the search bar 

![image](https://github.com/user-attachments/assets/095f7330-648c-4146-9201-0bbdd08845fe)

4.To access the folder's location, use the cd command to change to the desired directory. Type cd and paste file path C:\Work Categories\Apprenticeship\Northeastern University\Intensive Foundations of Computer Science\Algebra-Simple-Equation-Program-main (1)\Algebra-Simple-Equation-Program-main

![image](https://github.com/user-attachments/assets/d028cacb-6d60-4e4f-bc61-5f46dea1f11f)

5.You can now open the python script by entering the following, 

```
python "Simple Algebra Equation Test.py"
``` 

![image](https://github.com/user-attachments/assets/6e3422d2-f7d2-4123-a13f-a94b4996e88e)

### Mac Steps to Run The Program

1.Ensure you have the Python 3.13.2 installed. You can install python using this link

```
https://www.python.org/downloads/
```

2.Download the ZIP file.Open Terminal and navigate to Downloads Directory by typing,

```
cd ~/Downloads
```

![image](https://github.com/user-attachments/assets/1f17cad7-c900-4fa6-92f8-4ff0ca482b09)

3.Unzip the folder by entering the following command,
```
 unzip -o Algebra-Simple-Equation-Program-main.zip
```
(Press 'A' when it asks to replace files) 

![image](https://github.com/user-attachments/assets/c6f39d9c-4d15-4c4c-9d6a-3736a890c1f2)

4.Enter the project folder by entering,
```
cd Algebra-Simple-Equation-Program-main 
```
![image](https://github.com/user-attachments/assets/b7c2f6e6-e4cb-46dc-bd73-ba1a14fc953e)

5.Run the program
```
python3 "Simple_Algebra_Equation_Test.py"
``` 

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

Displays a welcome message.
```
print("Welcome To The Algebra Equation Test") 
```
I created a variable “name=input()” which will prompt the user to enter their name. 
```
name = input("Enter your name: ") 
```
Uses an f-string to personalize the welcome message. It takes the input of the user's name and substitute that into the print string
```
print(f"Welcome, {name}! Let's test your algebra skills today.\n") 
```
Lastly the last print function lets the user know to ‘Solve for x in each line’ and i added \n which will create a new line for the next set of codes.
```
print("Solve for x in each equation. You Got This! \n") 
```

### Defining Equations

![image](https://github.com/user-attachments/assets/b36ef6e2-f421-4aa9-a208-7ec9afadee73)
```
Import Random 
```
i imported the Random module which is a library which is used to generate random numbers. I required to import this module to create the two defined function make_a_equation1 and make_a_equation2. 

```make_a_equation1() ```

Generates a multiplication equation in the form: y * x = a 

Uses ```random.randint(-5, 10)``` to pick random integers for y and x. 

Returns: 

The equation string ```(f"{y} * x = {a}")``` 

The correct answer ```(x)``` 

```make_a_equation2()```

Generates an addition equation in the form: d + x = g 

Uses ```random.randint(-5, 10)``` for d and x. 

Returns: 

The equation string ```(f"{d} + x = {g}")```

The correct answer ```(x)``` 

For each defined function i made sure it returns the equation string which is ```(‘{y} * x = {g})``` and return the answer ```(‘x’)```. As both return functions are in f strings for each question it will generate a different equation with different numbers. 

### Creating User Input Function 

![image](https://github.com/user-attachments/assets/fc8eace6-2d86-40d0-a897-238499e8fd57)

The function ```get_user_guess(equation)``` ensures the user provides a valid integer answer. 

I created a function that asks the user to solve the equation using 

 ```
int(input (f"Solve for x: {equation}\nYour answer: ")) 
```

 For this function, I used a while True loop to create an infinite loop. Below this, I added a try block, which ensures the user inputs a valid integer. If they enter text or a float, it raises an error. That’s where the except block comes in it catches the error and returns to the original try command, prompting the user again until the correct input is entered. 

### Quiz Execution 

![image](https://github.com/user-attachments/assets/dc407515-4792-4b6e-8644-88942026c83e)

I then setup the quiz by setting up the start score number which is 
```
score = 0
```
and number of questions
```
test_question = 5
```
![image](https://github.com/user-attachments/assets/34acf497-1b44-4ce8-8405-6a62cee9bf72)

In this part of the code i used
```
‘for i in range(range(test_questions)’
```
which is a for loop that iterated over a sequences of numbers.The loop runs 5 times because test_questions  is equal to 5. This means that loop will take the range which goes from 0-5 meaning the loop will execute 5 times once per question. The variable i takes values from 0,1,2,3,4 ( 5 questions). Starts at i = 0 then i = 1 until it completes the iteration. 
```
equation_type = random.choice([1, 2])
```
The loop will randomly select the equation type ```make_a_equation1``` or ```make_a_equation2```. 

Depending on the selection: 

```If equation_type == 1```, it calls make_a_equation1(). 

```Else```, it calls ```make_a_equation2()```. 

Within the line ```equation, correct_answer = make_a_equation1()```, the function ```make_a_equation1()``` returns both the equation as a string and the correct answer. The equation variable stores the string representation of the equation, while ```correct_answer``` holds the value of ```x```. This means that when the equation is displayed, it replaces ```{equation}``` with the generated equation, and ```correct_answer``` will now contain the correct value of x for validation. 

```
else: 

equation, correct_answer = make_a_equation2()
``` 

If the equation type 1 is not selected it will select choice 2 which is the second type of equation, we created which is ```make_a_equation2```.

The user’s answer is checked against the correct answer
```
user_answer = get_user_guess(equation)

if user_answer == correct_answer: 
        print("✅Correct!\n") 
        score += 1
```
If correct: 

```Prints "✅Correct!\n"```

and Increments the score by 1. 

If incorrect: 

```Prints(f"❌Wrong! The correct answer was {correct_answer}.\n")```

### Final Score & End of Test

![image](https://github.com/user-attachments/assets/265b1658-d294-468a-b789-e2e4a3d4b57e)

Now that equation stores the generated problem, the program checks the user’s answer. The function ```get_user_guess(equation)``` captures their input as user_answer. If ```user_answer``` matches ```correct_answer```, it prints ✅ Correct! and adds 1 to score. If wrong, it prints ❌ Wrong! along with the correct answer using an f-string ({correct_answer}). 

Finally, it displays their total score ```({score}/{test_questions})``` and thanks them for completing the test.





















