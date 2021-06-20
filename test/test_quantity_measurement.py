from main.quantity_measurement import Feet, Inch, Yard

"""Tested the followings according to the testcase."""


def test_given_zero_feet_and_zero_feet_when_compared_should_return_true():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet


def test_given_zero_feet_and_none_when_compared_should_return_false():
    first_feet = Feet(0.0)
    assert first_feet is not None


def test_given_two_same_feet_values_when_compared_reference_should_return_true():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet


def test_given_zero_feet_and_float_value_when_compared_should_return_false():
    first_feet = Feet(0.0)
    second_feet = float(0.0)
    assert first_feet != second_feet


def test_given_one_feet_and_one_feet_when_compared_should_return_true():
    first_feet = Feet(1.0)
    second_feet = Feet(1.0)
    assert first_feet == second_feet


def test_given_zero_inch_and_none_when_compared_should_return_false():
    first_inch = Inch(0.0)
    assert first_inch is not None


def test_given_two_same_inch_values_when_compared_reference_should_return_true():
    first_inch = Inch(0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_given_zero_inch_and_float_value_when_compared_should_return_false():
    first_inch = Inch(0.0)
    second_inch = float(0.0)
    assert first_inch != second_inch


def test_given_zero_inch_and_zero_inch_when_compared_should_return_true():
    first_inch = Inch(0.0)
    second_inch = Inch(0.0)
    assert first_inch == second_inch


def test_given_zero_feet_and_zero_inch_when_compared_should_return_true():
    first_feet = Feet(0.0)
    second_inch = Inch(0.0)
    assert first_feet == second_inch


def test_given_one_inch_and_one_feet_when_compared_should_return_false():
    first_feet = Feet(1)
    second_inch = Inch(1)
    assert first_feet != second_inch


def test_given_one_feet_and_one_inch_when_compared_should_return_true():
    first_inch = Inch(1)
    second_feet = Feet(1)
    assert first_inch != second_feet


def test_given_one_feet_and_twelve_inch_when_compared_should_return_true():
    feet = Feet(1)
    inch = Inch(12)
    assert feet == inch


def test_given_twelve_inch_and_one_feet_when_compared_should_return_true():
    inch = Inch(12)
    feet = Feet(1)
    assert inch == feet


def test_given_three_feet_and_one_yard_when_compared_should_return_true():
    feet = Feet(3)
    yard = Yard(1)
    assert feet == yard


def test_given_one_feet_and_one_yard_when_compared_should_return_false():
    feet = Feet(1)
    yard = Yard(1)
    assert feet != yard


def test_given_one_inch_and_one_yard_when_compared_should_return_false():
    inch = Inch(1)
    yard = Yard(1)
    assert inch != yard


def test_given_one_yard_and_36_inch_when_compared_should_return_true():
    yard = Yard(1)
    inch = Inch(36)
    assert yard == inch


def test_given_36_inch_and_one_yard_when_compared_should_return_true():
    inch = Inch(36)
    yard = Yard(1)
    assert inch == yard


def test_given_one_yard_and_three_feet_when_compared_should_return_true():
    yard = Yard(1)
    feet = Feet(3)
    assert yard == feet
