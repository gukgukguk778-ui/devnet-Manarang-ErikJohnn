"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Erik John D. Manarang  
Date: 9/25/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is the way a program decides what to do. I think of control flow, as a map that shows the path a program takes. In Python the if, elif and else statements are used to make control flow decisions. The if statement checks a condition. If that condition is true Python runs the code inside that block. I notice that the elif statement means "else if" and lets us check another condition when the previous one was false. The else statement runs when none of the conditions are true. For example a program can check a student’s grade. Show whether the student passed, needs improvement or failed. This lets the control flow respond differently based on the information it receives.


============================================
KEY VOCABULARY
============================================
- condition: A statement that the program checks to see if something is true or false.
- if / elif / else: if - Used to run a block of code when a condition is true, elif - Short, for " if." It checks another condition only if the IF or elif condition did not work, else - Runs when all previous conditions are false.
- comparison operator: A comparison symbol helps me compare values. A comparison symbol such, as > < == !=, >= and <= is used.
- boolean expression: An expression that produces either True or False.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

battery_percent = 18

if battery_percent > 80:
    print("Battery is fully charged.")
elif battery_percent > 20:
    print("Battery level is good.")
elif battery_percent > 10:
    print("Low Battery! Please connect your charger.")
else:
    print("Critical Battery! Phone is about to shut down.")



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is confusing the assignment operator (=) with 
the comparison operator (==). Using a single '=' inside an 'if' condition will 
cause a SyntaxError because '=' assigns a value instead of comparing it.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
