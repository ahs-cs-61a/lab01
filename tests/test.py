# lab01 tests


# IMPORTS

import labs.lab01 as lab
import tests.wwpd_storage as s
from io import StringIO 
import sys
import git

st = s.wwpd_storage 


# CAPTURING PRINTS (STDOUT) - https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43m'
    HIGH_RED = '\u001b[41m'
    HIGH_BLUE = '\u001b[44m'
    MAGENTA = ' \u001b[35m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'


# TESTS

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
    print("\n\nfizzbuzz(16) prints:")
    with Capturing() as fizzbuzz_16_output:
        lab.fizzbuzz(16)
    fizzbuzz_16 = ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16']
    if fizzbuzz_16 != fizzbuzz_16_output:
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR: Incorrect prints from fizzbuzz(16)" + bcolors.ENDC)
        assert fizzbuzz_16 == fizzbuzz_16_output
        
    if lab.fizzbuzz(16) is not None:
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR: Print, do not return." + bcolors.ENDC)
        assert lab.fizzbuzz(16) is None 


def test_has_digit():
    assert lab.has_digit(10, 1) == True
    assert lab.has_digit(12, 7) == False
    assert lab.has_digit(4, 4) == True


def test_unique_digits():
    assert lab.unique_digits(8675309) == 7
    assert lab.unique_digits(1313131) == 2
    assert lab.unique_digits(13173131) == 3
    assert lab.unique_digits(10000) == 2
    assert lab.unique_digits(101) == 2
    assert lab.unique_digits(10) == 2


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
    print("\n\nhailstone(10) prints:")
    with Capturing() as hailstone_10_output:
        lab.hailstone(10)
    hailstone_10 = ['10', '5', '16', '8', '4', '2', '1']
    if hailstone_10 != hailstone_10_output:
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR: Incorrect prints from hailstone(10)" + bcolors.ENDC)
        assert hailstone_10 == hailstone_10_output
    assert lab.hailstone(10) == 7

    print("\n\nhailstone(1) prints:")
    with Capturing() as hailstone_1_output:
        lab.hailstone(1)
    hailstone_1 = ['1']
    if hailstone_1 != hailstone_1_output:
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR: Incorrect prints from hailstone(1)" + bcolors.ENDC)
        assert hailstone_1 == hailstone_1_output
    assert lab.hailstone(1) == 1


# CHECK WWPD? IS ALL COMPLETE

def test_wwpd():
    assert len(st) == 41


# AUTO-COMMIT WHEN ALL TESTS ARE RAN

def test_commit():
    try:
        # IF CHANGES ARE MADE, COMMIT TO GITHUB
        user = input("\n\nWhat is your GitHub username (exact match, case sensitive)?\n")
        repo = git.Repo("/workspaces/lab01-" + user)
        repo.git.add('--all')
        repo.git.commit('-m', 'update lab')
        origin = repo.remote(name='origin')
        origin.push()
        print(bcolors.HIGH_GREEN + bcolors.BOLD + "\nSUCCESS: Lab complete and changes successfully committed." + bcolors.ENDC)
    except: 
        # IF CHANGES ARE NOT MADE, NO COMMITS TO GITHUB
        print(bcolors.HIGH_MAGENTA + bcolors.BOLD + "\nMESSAGE: Already up to date. No updates committed." + bcolors.ENDC)