from ahs_lab01 import a_plus_abs_b

def test():
    assert a_plus_abs_b(2, 3) == 5
    assert a_plus_abs_b(2, -3) == 5
    assert a_plus_abs_b(-1, -4) == 3
    assert a_plus_abs_b(-1, 4) == 3