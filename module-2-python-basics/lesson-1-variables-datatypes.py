"""
Module 2 — Lesson 1: Variables & Data Types
Student: Manarang, Erik John D.
Date: 9/25/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Variables and data types are concepts in programming. Variables are like boxes that can hold a value. These boxes have a name. Can change their value while a program runs. A variable might store a persons name, age or grade. A data type is a way to classify a value. Knowing the data type of a variable is important. Different data types are used for tasks. For example a persons age can be stored as an integer in one variable while the persons name can be stored as a string in another variable. Understanding variables and data types is important, to programmers. Programs often need to store and process different kinds of information.


============================================
KEY VOCABULARY
============================================
- variable: A name that refers to a value stored in a program. It lets us save information and use it again later.
- data type: A name that refers to a value stored in a program. It lets us save information and use it again later.
- int: A number that does not have a point, like 18 or 50 or 100.
- float: A number that has a dot in it, like 95.5 or 3.14
- string: A sequence of characters. Strings are usually written inside quotation marks. such as "ERIK"
- boolean: A value that can only be True or False. It is often used for conditions or decisions. This kind of value helps make choices in programs. When something is True it means the condition is met. When it is False the condition is not met. It plays a role, in making programs work the way we want them to.


(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

student_name = "Erik John D. Manarang" 
student_age = 20 average_grade = 95.1 
is_enrolled = True 
print("Student Name:", student_name) 
print("Age:", student_age) 
print("Average Grade:", average_grade) 
print("Currently Enrolled:", is_enrolled)  

print(type(student_name)) 
print(type(student_age)) 
print(type(average_grade)) 
print(type(is_enrolled))


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is confusing strings with numbers. I have learned that this mistake can lead to bugs.

Age = "20"

Here 20 is a string because it is inside quotation marks. It is not an integer.

If I write:

age = 20

then age is an integer, which means I can use it for calculations.

Another mistake I want to avoid is using the data type for a task.

Understanding the difference, between strings, integers, floats and booleans helps prevent errors in a program.



============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
