# lab01 tests


# IMPORTS

import labs.lab01 as lab, tests.wwpd_storage as s
import sys, git, math, time
from io import StringIO 

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
    MAGENTA = ' \u001b[35m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33;1m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'
    
def print_error(message):
    print("\n" + bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR:" + bcolors.RESET + bcolors.YELLOW + bcolors.BOLD + " " + message + bcolors.ENDC)

def print_message(message):
    print("\n" + bcolors.HIGH_MAGENTA + bcolors.BOLD + "MESSAGE:" + bcolors.RESET + bcolors.MAGENTA + bcolors.BOLD + " " + message + bcolors.ENDC)

def print_success(message):
    print("\n" + bcolors.HIGH_GREEN + bcolors.BOLD + "SUCCESS:" + bcolors.RESET + bcolors.GREEN + bcolors.BOLD + " " + message + bcolors.ENDC)


# TESTS

correct = [0]

def test_falling():
    assert lab.falling(6, 3) == 120
    assert lab.falling(4, 3) == 24
    assert lab.falling(4, 1) == 4
    assert lab.falling(4, 0) == 1

    correct[0] += 1


def test_sum_digits():
    assert lab.sum_digits(10) == 1
    assert lab.sum_digits(4224) == 12
    assert lab.sum_digits(1234567890) == 45

    correct[0] += 1    


def test_double_eights():
    assert not lab.double_eights(8)
    assert lab.double_eights(88)
    assert lab.double_eights(2882)
    assert lab.double_eights(880088)
    assert not lab.double_eights(12345)
    assert not lab.double_eights(80808080)

    correct[0] += 1


def test_wears_jacket_with_if():
    assert not lab.wears_jacket_with_if(90, False)
    assert lab.wears_jacket_with_if(40, False)
    assert lab.wears_jacket_with_if(100, True)

    correct[0] += 1


def test_is_prime():
    assert not lab.is_prime(10)
    assert lab.is_prime(7)
    assert not lab.is_prime(1)

    correct[0] += 1


def test_fizzbuzz():
    print("\n\nfizzbuzz(16) prints:")
    with Capturing() as fizzbuzz_16_output:
        lab.fizzbuzz(16)
    fizzbuzz_16 = ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16']
    if fizzbuzz_16 != fizzbuzz_16_output:
        print_error("Incorrect prints from fizzbuzz(16)")
        assert fizzbuzz_16 == fizzbuzz_16_output
        
    if lab.fizzbuzz(16) is not None:
        print_error("Print, do not return.")
        assert lab.fizzbuzz(16) is None 

    correct[0] += 1


def test_has_digit():
    assert lab.has_digit(10, 1)
    assert not lab.has_digit(12, 7)
    assert lab.has_digit(4, 4)
    
    correct[0] += 1


def test_unique_digits():
    assert lab.unique_digits(8675309) == 7
    assert lab.unique_digits(1313131) == 2
    assert lab.unique_digits(13173131) == 3
    assert lab.unique_digits(10000) == 2
    assert lab.unique_digits(101) == 2
    assert lab.unique_digits(10) == 2

    correct[0] += 1


def test_a_plus_abs_b():
    assert lab.a_plus_abs_b(2, 3) == 5
    assert lab.a_plus_abs_b(2, -3) == 5
    assert lab.a_plus_abs_b(-1, -4) == 3
    assert lab.a_plus_abs_b(-1, 4) == 3

    correct[0] += 1


def test_two_of_three():
    assert lab.two_of_three(1, 2, 3) == 5
    assert lab.two_of_three(5, 3, 1) == 10
    assert lab.two_of_three(10, 2, 8) == 68
    assert lab.two_of_three(5, 5, 5) == 50

    correct[0] += 1


def test_largest_factor():
    assert lab.largest_factor(15) == 5
    assert lab.largest_factor(80) == 40
    assert lab.largest_factor(13) == 1

    correct[0] += 1


def test_hailstone():
    print("\n\nhailstone(10) prints:")
    with Capturing() as hailstone_10_output:
        lab.hailstone(10)
    hailstone_10 = ['10', '5', '16', '8', '4', '2', '1']
    if hailstone_10 != hailstone_10_output:
        print_error("Incorrect prints from hailstone(10)")
    assert hailstone_10 == hailstone_10_output
    assert lab.hailstone(10) == 7

    print("\n\nhailstone(1) prints:")
    with Capturing() as hailstone_1_output:
        lab.hailstone(1)
    hailstone_1 = ['1']
    if hailstone_1 != hailstone_1_output:
        print_error("Incorrect prints from hailstone(1)")
    assert hailstone_1 == hailstone_1_output
    assert lab.hailstone(1) == 1

    correct[0] += 1


# CHECK WWPD? IS ALL COMPLETE

wwpd_complete = True

def test_wwpd():
    if len(st) != 41 or not all([i[4] for i in st]):
        print_error("WWPD? is incomplete.")
        wwpd_complete = False
    assert len(st) == 41
    assert all([i[4] for i in st])

    correct[0] += 1


<<<<<<< HEAD
# AUTO-COMMIT WHEN ALL TESTS ARE RAN

user = []

def test_commit():
    try:
        # IF CHANGES ARE MADE, COMMIT TO GITHUB
        repo = git.Repo("/c/Users/rober/OneDrive/Desktop/ahs-cs-61a github/local_testing")
        repo.git.add('--all')
        repo.git.commit('-m', 'update lab')
        origin = repo.remote(name='origin')
        origin.push()
        print_success("Changes successfully committed.")  
    # except git.GitCommandError: 
    #     # IF CHANGES ARE NOT MADE, NO COMMITS TO GITHUB
    #     print_message("Already up to date. No updates committed.")
    except git.NoSuchPathError:
        # IF GITHUB USERNAME IS NOT FOUND
        print_error("Incorrect GitHub username; try again.")
        raise git.NoSuchPathError("")
    

=======
>>>>>>> f85ed86f9a4bc93b353b65a9f8e9e65842aa6684
# PRINT PROGRESS BAR

def test_progress_bar():
    num_correct, total = correct[0], 13
    percent_correct = num_correct / total * 100

    print("\n\n" + bcolors.HIGH_MAGENTA + bcolors.BOLD + "PROGRESS BAR:" + bcolors.ENDC)

    for i in range(0, 54):
        print(int(i * 10 / 5), end = '') if i % 5 == 0 else print(" ", end = '')
    print()

    print(bcolors.BOLD + "<" + bcolors.ENDC, end = '')
    i = 0
    while i < 60:
        time.sleep(0.02)
        if i / 60 * 100 < percent_correct:
            print(bcolors.GREEN + bcolors.BOLD + "■" + bcolors.ENDC, end = '', flush = True)
        else:
            print(bcolors.YELLOW + bcolors.BOLD + "■" + bcolors.ENDC, end = '', flush = True)
        i += 1
    print(bcolors.BOLD + ">" + bcolors.ENDC)

    time.sleep(2.5)  


# AUTO-COMMIT WHEN ALL TESTS ARE RAN

user = []

def test_commit():
    try:
        # IF CHANGES ARE MADE, COMMIT TO GITHUB
        repo = git.Repo("C:/Users/rober/OneDrive/Desktop/ahs-61a github/local_testing/lab01")
        repo.git.add('--all')
        repo.git.commit('-m', 'update lab')
        origin = repo.remote(name='origin')
        origin.push()
        print_success("Changes successfully committed.")  
    except git.GitCommandError: 
        # IF CHANGES ARE NOT MADE, NO COMMITS TO GITHUB
        print_message("Already up to date. No updates committed.")
    except git.NoSuchPathError:
        # IF GITHUB USERNAME IS NOT FOUND
        print_error("Incorrect GitHub username; try again.")
        raise git.NoSuchPathError("")