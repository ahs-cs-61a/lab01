from ahs_lab01 import double_eights

def test():
    assert double_eights(8) == False
    assert double_eights(88) == True
    assert double_eights(2882) == True
    assert double_eights(880088) == True
    assert double_eights(12345) == False
    assert double_eights(80808080) == False