from app import add_two_numbers


def test_add_two_numbers_with_positive_values():
    assert add_two_numbers(5, 10) == 15


def test_add_two_numbers_with_negative_value():
    assert add_two_numbers(-2, 5) == 3


def test_add_two_numbers_with_zero():
    assert add_two_numbers(0, 0) == 0