import re

def license_plate_checker(plate, pattern):
#Here I have created a function that takes two arguements (plate, pattern), and brings them through a plate checker.
    if re.match(pattern, plate):
        return "License plate found"
    else:
        return "License plate not found"
"""
Here I have created an if statement that uses the re.match function. 
Since this is using the same two arguments as the def function. 
It will take the users input and see if it matches the same pattern that I have written below.
If it does, it will return "License plate found". and if it doesn't then it will return "License plate not found".
"""

Pattern = r'^[A-Z]{2}\d{2} [A-Z]{3}$'
#Here I have used the re library to implement a pattern that the checker will use in its match statement.

Plate = input("Input your plate number here: ")
#This is me asking for the users input

print(license_plate_checker(Plate, Pattern))
#This will bring the argument given by the user through the checker, and then bring it back down to be printed.