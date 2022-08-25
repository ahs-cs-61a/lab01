from ahs_lab01 import unique_digits

def test():

    assert unique_digits(8675309) == 7
    assert unique_digits(1313131) == 2
    assert unique_digits(13173131) == 3
    assert unique_digits(10000) == 2
    assert unique_digits(101) == 2
    assert unique_digits(10) == 2