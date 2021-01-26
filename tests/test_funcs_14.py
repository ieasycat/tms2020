from funcs import funcs_14


def test_inches_centimeters():
    assert funcs_14.inches_centimeters(10) == 25.4


def test_centimeters_inches():
    assert funcs_14.centimeters_inches(25.4) == 10


def test_miles_kilometers():
    assert funcs_14.miles_kilometers(10) == 16.093470878864444


def test_kilometers_miles():
    assert funcs_14.kilometers_miles(16.093470878864444) == 10


def test_pounds_kilograms():
    assert funcs_14.pounds_kilograms(10) == 4.535970244035199


def test_kilograms_pounds():
    assert funcs_14.kilograms_pounds(4.535970244035199) == 10


def test_ounces_grams():
    assert funcs_14.ounces_grams(10) == 283.4949254408346


def test_grams_ounces():
    assert funcs_14.grams_ounces(283.4949254408346) == 10


def test_gallon_liters():
    assert funcs_14.gallon_liters(10) == 37.85441193171064


def test_liters_gallon():
    assert funcs_14.liters_gallon(37.85441193171064) == 10


def test_pints_liters():
    assert funcs_14.pints_liters(10) == 5.682463916354131


def test_liters_pints():
    assert funcs_14.liters_pints(5.682463916354131) == 10
