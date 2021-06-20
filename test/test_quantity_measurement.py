from main.quantity_measurement import Feet, Inch

"""Tested the followings according to the testcase."""


def test_givenZeroFtAndZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet


def test_givenZeroFtAndNone_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(0.0)
    assert first_feet is not None


def test_givenTwoSameFeetValues_WhenComparedForReference_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet


def test_givenZeroFtAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(0.0)
    second_feet = float(0.0)
    assert  first_feet != second_feet


def test_givenOneFtAndOneFt_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(1.0)
    second_feet = Feet(1.0)
    assert first_feet == second_feet


def test_givenZeroInchAndNone_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(0.0)
    assert first_inch is not None


def test_givenTwoSameInchValues_WhenComparedForReference_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_givenZeroInchAndFloatValue_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(0.0)
    second_inch = float(0.0)
    assert  first_inch != second_inch


def test_givenZeroInchAndZeroInch_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = Inch(0.0)
    assert first_inch == second_inch


def test_givenZeroFeetAndZeroInch_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_inch = Inch(0.0)
    assert first_feet == second_inch


def test_givenOneInchAndOneFeet_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(1)
    second_inch = Inch(1)
    assert first_feet != second_inch


def test_givenOneFeetAndOneInch_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(1)
    second_feet = Feet(1)
    assert first_inch != second_feet


def test_givenOneFtAndTwelveInch_WhenCompared_ShouldReturnTrue():
    feet = Feet(1)
    inch = Inch(12)
    assert feet == inch


def test_givenTwelveInchAndOneFt_WhenCompared_ShouldReturnTrue():
    inch = Inch(12)
    feet = Feet(1)
    assert inch == feet
