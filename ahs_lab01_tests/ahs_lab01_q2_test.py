from ahs_lab01 import sum_digits

def test():
    assert sum_digits(10) == 1
    assert sum_digits(4224) == 12
    assert sum_digits(1234567890) == 45