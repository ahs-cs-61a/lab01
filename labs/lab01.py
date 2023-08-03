# lab01: variables, control, functions

from operator import add, sub


# disc01: https://inst.eecs.berkeley.edu/~cs61a/su22/disc/disc01/

def wears_jacket_with_if(temp, raining): # q1
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return temp < 60 or raining


def is_prime(n): # q2
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 0 or n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def fizzbuzz(n): # q3
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
        i += 1


def has_digit(n, k): # q4
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"

    "*** YOUR CODE HERE ***"
    while n > 0:
        if n % 10 == k:
            return True
        n //= 10
    return False


def unique_digits(n):  # q5, use has_digit
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n > 0:
        curr = n % 10
        if not has_digit(n // 10, curr):
            count += 1
        n //= 10
    return count


# lab01: https://inst.eecs.berkeley.edu/~cs61a/su22/lab/lab01/

def falling(n, k): # q6
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    product = 1
    while k > 0:
        product *= n
        n -= 1
        k -= 1
    return product


def sum_digits(y): # q7
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while y > 0:
        sum += y % 10
        y //= 10
    return sum


def double_eights(n): # q8
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    num_eights = 0
    while n > 0:
        if num_eights and n % 10 == 8:
            return True
        else:
            num_eights = 0
        if n % 10 == 8:
            num_eights += 1
        n //= 10
    return False


# hw01: https://inst.eecs.berkeley.edu/~cs61a/su22/hw/hw01/

def a_plus_abs_b(a, b): # q9
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(i, j, k): # q10
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return min(i, j) ** 2 + min(j, k) ** 2 + min(i, k) ** 2 - min(i**2, j**2, k**2)
    
    # alternative: return min(i, j) ** 2 + min(max(i, j), k) ** 2


def largest_factor(n): # q11
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    div_num = 1
    largest_div = 1
    while div_num < n:
        if n % div_num == 0:
            largest_div = div_num
        div_num += 1
    return largest_div


def hailstone(n): # q12
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    num_steps = 1
    if n == 1:
        print(1)
    else:
        print(n)
        while not n == 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
            print(n)
            num_steps += 1
    return num_steps
