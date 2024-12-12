#This will be my hp-to-weight calculator (libraries, testing)
from pyCar import Car
#Here I am reffering back to the library I made, and I am calling back to the class within it.

def user_car_input():
    car = input("What is the car you want to check? ")
    horsepower = float(input("Input the cars horsepower: "))
    weight = float(input("Input the cars weight: "))
    return car, horsepower, weight
#This function is dedicated to getting the user's input, so that they can input their own car into the calculator, and find out the horsepower to weight ratio.
#I have called these the same names as the data I created in the library so that they match up. And I have ensured to make the horsepower and weight both floats, so that the user is able to enter the exact number.
#I have then used the return function so that I am able to pull this data into the function below.

def main():
    car, horsepower, weight = user_car_input()
    vehicle = Car(car, horsepower, weight)
    vehicle.ratio_result()
#Here I have created my main function. Which will pull the data from the user_car_input, using, the variables within the return function.
#I have then used the class within the library I made, and input the three variables that the user will give the program, and named it a single variable "vehicle".
#Finally I have made a function called vehicle.ratio_result(), which will call back to the library I made, specifically the result function, and it will give the user an output based on the data within the "vehicle" variable.

if __name__ == "__main__":
    main()
#This is the final part of the code, and I have used the if__name__=="__main__" function so that I am able to test this file in a seperate file to ensure that it is working.