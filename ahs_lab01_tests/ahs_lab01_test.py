from ahs_lab01 import falling, sum_digits, double_eights, wears_jack_with_if, is_prime, fizzbuzz, unique_digits, has_digit, a_plus_abs_b, two_of_three, largest_factor, hailstone

def test(): 
    #q1
    assert falling(6, 3) == 120
    assert falling(4, 3) == 24
    assert falling(4, 1) == 4
    assert falling(4, 0) == 1

    #q2
    assert sum_digits(10) == 1
    assert sum_digits(4224) == 12
    assert sum_digits(1234567890) == 45

    #q3
    assert double_eights(8) == False
    assert double_eights(88) == True
    assert double_eights(2882) == True
    assert double_eights(880088) == True
    assert double_eights(12345) == False
    assert double_eights(80808080) == False

    #q4
    assert wears_jacket_with_if(90, False) == False
    assert wears_jacket_with_if(40, False) == True
    assert wears_jacket_with_if(100, True) == True

    #q5
    assert is_prime(10) == False
    assert is_prime(7) == True
    assert is_prime(1) == False

    #q6
    assert fizzbuzz(16) is None

    #q7
    assert unique_digits(8675309) == 7
    assert unique_digits(1313131) == 2
    assert unique_digits(13173131) == 3
    assert unique_digits(10000) == 2
    assert unique_digits(101) == 2
    assert unique_digits(10) == 2

    #q8
    assert has_digit(10, 1) == True
    assert has_digit(12, 7) == False
    assert has_digit(4, 4) == True

    #q9
    assert a_plus_abs_b(2, 3) == 5
    assert a_plus_abs_b(2, -3) == 5
    assert a_plus_abs_b(-1, -4) == 3
    assert a_plus_abs_b(-1, 4) == 3

    #q10
    assert two_of_three(1, 2, 3) == 5
    assert two_of_three(5, 3, 1) == 10
    assert two_of_three(10, 2, 8) == 68
    assert two_of_three(5, 5, 5) == 50

    #q11
    assert largest_factor(15) == 5
    assert largest_factor(80) == 40
    assert largest_factor(13) == 1

    #q12
    assert hailstone(10) == 7
    assert hailstone(1) == 1
