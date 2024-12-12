#This will be my own library (libraries, Object Orientated Programming)
class Car:
    def __init__(self, car, horsepower, weight):
        self.car = car
        self.horsepower = horsepower
        self.weight = weight
#Here I have created a function method inside a class. This is so that I am able to create my own data.
#This data will include the three main variables within my hp-to-weight calculator, being the car, horsepower, and weight.

    def ratio_calculator(self):
        if self.weight == 0:
            raise ZeroDivisionError("The weight of a car cannot be zero")
        else:
            ratio = (self.horsepower / self.weight)
            return ratio
#This is the ratio calculator for the hp-to-weight. I have added a form of error handling, using an if statement, since we cannot divide by zero, and the weight of a car cannot be zero.
#I have then created a new variable called ratio. And referred back to the data I created in the first function, and made a formula for the hp-to-weight ratio. 

    def ratio_result(self):
        if self.horsepower == 0:
            print("The horsepower of a car cannot be zero")
        else:
            print(f"Horsepower-to-weight Ratio: {self.ratio_calculator()} HP/kg")
#Here I have created the output. I have first ensured that it is known that the horsepower of a car cannot be zero, so I have used an if statement here again.
#And then for the else statement, it will print out a string, followed by the data gathered, and then followed by the units of hp-to-weight.