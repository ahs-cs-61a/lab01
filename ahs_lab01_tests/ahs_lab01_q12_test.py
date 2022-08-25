from ahs_lab01 import hailstone

def test():
    assert hailstone(10) == 7
    assert hailstone(1) == 1
