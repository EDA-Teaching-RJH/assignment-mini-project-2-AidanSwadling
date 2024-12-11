from pyCar import Car

def user_car_input():
    car = input("What is the car you want to check? ")
    horsepower = float(input("Input the cars horsepower: "))
    weight = float(input("Input the cars weight: "))
    return car, horsepower, weight

def main():
    car, horsepower, weight = user_car_input()
    vehicle = Car(car, horsepower, weight)
    vehicle.ratio_result()

if __name__ == "__main__":
    main()
