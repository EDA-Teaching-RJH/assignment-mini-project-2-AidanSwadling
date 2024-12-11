class Car:
    def __init__(self, car, horsepower, weight):
        self.car = car
        self.horsepower = horsepower
        self.weight = weight

    def ratio_calculator(self):
        if self.weight == 0:
            raise ZeroDivisionError("The weight of a car cannot be zero")
        else:
            ratio = (self.horsepower / self.weight)
            return ratio

    def ratio_result(self):
        if self.horsepower == 0:
            print("The horsepower of a car cannot be zero")
        else:
            print(f"Horsepower-to-weight Ratio: {self.ratio_calculator()} HP/kg")