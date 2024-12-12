#This will be my testing file (testing)
from pyCar import Car
import pytest
#Here I am referring back to the library I made, while also using the pytest library, so that I am able to write the test code in the terminal.

def test_ratio_calculator():
    ferrari = Car("Ferrari LaFerrari", 500, 2000)
    assert ferrari.ratio_calculator() == 0.25
#Here I have created a test variable called ferrari, which is exactly the same as the vehicle variable, where it will call back to the calculator, and check whether the information I have put is correct.

    porsche = Car("Porsche 911 GT3 RS", 0, 1450)
    assert porsche.ratio_calculator() == 0
#Here I have created a variable which is the same as the ferrari one, but it is making sure that when the horsepower is 0, it actually returns 0.

    lamborghini = Car("Lamborghini Huracan", 2000, 500)
    assert lamborghini.ratio_calculator() == 4
#Finally I have created a variable named lamborghini that will check whether the result can be over 1, which in this case it should be able to.
