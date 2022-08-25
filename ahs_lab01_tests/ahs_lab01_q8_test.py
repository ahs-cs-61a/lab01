from ahs_lab01 import unique_digits, has_digit

def test():
    assert has_digit(10, 1) == True
    assert has_digit(12, 7) == False
    assert has_digit(4, 4) == True