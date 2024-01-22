# Exercise 10: Create a new list from two list using the following condition
# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# Given: 
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# Expected Output:
# result list: [25, 35, 40, 60, 90]

# Pseudocode 

# Create a function that will combine the odd from first list and even from second list
def combine(list1, list2): 

# Create a variable that have empty list 
    result_list = []

# Create a loop and add condition to find the odd number in list1 
    for i in list1:
        if i % 2 != 0:
            result_list.append(i)

# Create a loop and add condition to find the even number in list2
# Input the given values in the lists and print the results 