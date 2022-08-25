from ahs_lab01 import two_of_three

def test():
    assert two_of_three(1, 2, 3) == 5
    assert two_of_three(5, 3, 1) == 10
    assert two_of_three(10, 2, 8) == 68
    assert two_of_three(5, 5, 5) == 50
    
