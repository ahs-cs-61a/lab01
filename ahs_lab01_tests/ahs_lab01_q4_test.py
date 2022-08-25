from ahs_lab01 import wears_jackets_with_if

def test():
    assert wears_jackets_with_if(90, False) == False
    assert wears_jackets_with_if(40, False) == True
    assert wears_jackets_with_if(100, True) == True
    