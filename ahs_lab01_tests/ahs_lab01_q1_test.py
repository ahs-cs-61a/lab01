from ahs_lab01 import falling

def test():
    assert falling(6, 3) == 120
    assert falling(4, 3) == 24
    assert falling(4, 1) == 4
    assert falling(4, 0) == 1