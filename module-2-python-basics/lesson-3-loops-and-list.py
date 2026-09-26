"""
Module 2 — Lesson 3: Loops & Lists
Student: Erik John D. Manarang
Date: 9/25/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Lists and loops are used when I have to handle a lot of data. A list is a container in which I can put values together. For example if I have the names of my classmates I can put all of their names into one list of creating a separate variable for each person. A loop is used when I want the program to repeat a task. A, for loop can go through each item in a list one by one. A while loop keeps running long as the condition remains true.


============================================
KEY VOCABULARY
============================================
- list: A list is a group of values that I can store together in one variable.
- for loop: A loop that automatically visits each item in a list from start to finish.
- while loop: A loop that keeps repeating as long as a condition remains True.
- index: The index is the position of an item, in a list. In Python the index starts at 0 for the position.
- iteration: a new version of a product or idea that results from such repetition
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# Daily Morning Tasks
tasks = ["Make the bed", "Brush teeth", "Eat breakfast", "Pack backpack"]

print("MORNING TO-DO LIST ")
for task in tasks:
    print("Done:", task)

print("Total tasks finished:", len(tasks))
print()

# Water intake tracker 
cups_drank = 0
daily_goal = 5

print("HYDRATION TRACKER ")
while cups_drank < daily_goal:
    cups_drank += 1
    print(f"Drank cup #{cups_drank}. Keep going!")

print("Goal reached! You are fully hydrated for the day.")



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is an off by one error in a while loop. For example if I start at cups_drank = 1. Use while cups_drank <= daily_goal and then increase the counter inside I might end up counting 6 cups instead of 5. I also want to make sure my code, inside the while loop is properly indented or Python will give me an IndentationError.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
