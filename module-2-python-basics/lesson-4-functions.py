"""
Module 2 — Lesson 4: Functions
Student: Erik John D. Manarang
Date: 9/25/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A function is like a recipe or a shortcut button on a microwave. Of writing down the same ten steps every time you want to do a task you write the steps once inside a function and give the function a name. Whenever you need that task done you simply call the functions name. Functions can also take in inputs called parameters like a blender takes in fruit. The function processes those inputs. Can give you back a final result called a return value, like a smoothie you can save in a cup and use later.


============================================
KEY VOCABULARY
============================================
- def: The keyword in Python used to create (define) a new function.
- function: A reusable block of code that performs a specific task when called.
- parameter: A variable in the function definition that acts as a placeholder for data.
- argument: The actual value you pass into the function when you call it.
- return: A keyword that sends the finished result back to the place where the function was called.
- call (or invoke): Running the function by typing its name followed by parentheses ().
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# Calling the function and saving the returned value
item_price = 50.00
tax = 0.08  

total_due = calculate_total(item_price, tax)
print(f"Total price to pay: ${total_due:.2f}")


# Simple helper function with a conditional check
def check_pass_fail(score):
    if score >= 75:
        return "Passed"
    else:
        return "Needs Retake"


print("Student A result:", check_pass_fail(82))
print("Student B result:", check_pass_fail(64))




"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is mixing up print() with return. Using print() inside a function just shows the result on the screen. It does not save the result for use. If I write result = calculate_total(50, 0.08) and the function uses print() of return the variable result will end up as None. I need to use return every time I want the function to give data back to the rest of the program. That way the data can be stored, reused or used in calculations. It’s important to remember that print() is, for showing things to the user. It’s not for passing values to variables or other parts of the code. So I must always use return when I need the function to send back a value.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
