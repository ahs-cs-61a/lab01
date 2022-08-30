import labs.lab01 as lab

def test_falling():
    assert lab.falling(6, 3) == 120
    assert lab.falling(4, 3) == 24
    assert lab.falling(4, 1) == 4
    assert lab.falling(4, 0) == 1

def test_sum_digits(): 
    assert lab.sum_digits(10) == 1
    assert lab.sum_digits(4224) == 12
    assert lab.sum_digits(1234567890) == 45

def test_double_eights(): 
    assert lab.double_eights(8) == False
    assert lab.double_eights(88) == True
    assert lab.double_eights(2882) == True
    assert lab.double_eights(880088) == True
    assert lab.double_eights(12345) == False
    assert lab.double_eights(80808080) == False

def test_wears_jacket_with_if(): 
    assert lab.wears_jacket_with_if(90, False) == False
    assert lab.wears_jacket_with_if(40, False) == True
    assert lab.wears_jacket_with_if(100, True) == True

def test_is_prime(): 
    assert lab.is_prime(10) == False
    assert lab.is_prime(7) == True
    assert lab.is_prime(1) == False

def test_fizzbuzz(): 
    assert lab.fizzbuzz(16) is None

def test_unique_digits(): 
    assert lab.unique_digits(8675309) == 7
    assert lab.unique_digits(1313131) == 2
    assert lab.unique_digits(13173131) == 3
    assert lab.unique_digits(10000) == 2
    assert lab.unique_digits(101) == 2
    assert lab.unique_digits(10) == 2

def test_has_digit():
    assert lab.has_digit(10, 1) == True
    assert lab.has_digit(12, 7) == False
    assert lab.has_digit(4, 4) == True

def test_a_plus_abs_b(): 
    assert lab.a_plus_abs_b(2, 3) == 5
    assert lab.a_plus_abs_b(2, -3) == 5
    assert lab.a_plus_abs_b(-1, -4) == 3
    assert lab.a_plus_abs_b(-1, 4) == 3

def test_two_of_three(): 
    assert lab.two_of_three(1, 2, 3) == 5
    assert lab.two_of_three(5, 3, 1) == 10
    assert lab.two_of_three(10, 2, 8) == 68
    assert lab.two_of_three(5, 5, 5) == 50

def test_largest_factor(): 
    assert lab.largest_factor(15) == 5
    assert lab.largest_factor(80) == 40
    assert lab.largest_factor(13) == 1

def test_hailstone(): 
    assert lab.hailstone(10) == 7
    assert lab.hailstone(1) == 1