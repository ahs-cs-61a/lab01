from ahs_lab01 import hailstone

def test():
    assert hailstone(10) is None
    assert hailstone(1)