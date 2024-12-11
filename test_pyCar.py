from pyCar import Car
import pytest

def test_ratio_calculator():
    ferrari = Car("Ferrari LaFerrari", 500, 2000)
    assert ferrari.ratio_calculator() == 0.25

    porsche = Car("Porsche 911 GT3 RS", 0, 1450)
    assert porsche.ratio_calculator() == 0

    lamborghini = Car("Lamborghini Huracan", 2000, 500)
    assert lamborghini.ratio_calculator() == 4

