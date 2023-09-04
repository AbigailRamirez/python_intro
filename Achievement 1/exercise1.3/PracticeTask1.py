'''
1. Make a simple script that does addition and subtraction between two numbers.
2. The user gets to input three items: the first value, the second value, 
and then the operator `+` or ``.
3. Based on the three inputs above, use `if-elif-else` statements to decide whether 
you’re going to perform addition or subtraction on the two values.
4. Use a final `else` statement to handle any unexpected operator. 
You could print a short error message like `"Unknown operator"`.
5. Create a folder for this Exercise on your Github repo (you can name it “Exercise 1.3”). 
Create a sub folder inside this folder and name it “1.3-Practice Task 1” or something similar. 
Upload the screenshots you captured for the previous steps in this folder.'''

value1 = int(input("Please enter a number: "))
operator = input("Select + or - : ")
value2 = int(input("Please enter your second number: "))

if operator == "+":
    print("The sum of the values is: ",value1+value2)
elif operator == "-":
    print("The subtraction of the values is: ", value1-value2)
else:
    print("Unknown Operator")