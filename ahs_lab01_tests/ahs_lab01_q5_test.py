from ahs_lab01 import is_prime

def test():
    assert is_prime(10) == False
    assert is_prime(7) == True
    assert is_prime(1) == False