# lab01 WWPD?

# IMPORTS

import inspect
import tests.wwpd_storage as s

st = s.wwpd_storage 

# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43;1m'
    HIGH_RED = '\u001b[41m'
    HIGH_BLUE = '\u001b[44m'
    MAGENTA = ' \u001b[35m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33;1m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'


# INCORRECT ANSWER LOOP, INSTRUCTIONS, COMPLETE, OPTIONS

def repeat():
    print("Try again:")
    return input()

def intro(name):
    print("\nWhat Would Python Display?: " + name)
    print("Type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed.\n")

def complete():
    print(bcolors.HIGH_GREEN + bcolors.BOLD + "\nSUCCESS: All questions for this question set complete." + bcolors.ENDC)

def options():

    print(bcolors.HIGH_MAGENTA + bcolors.BOLD + "\nMESSAGE: All questions for this question set complete. Restart question set?" + bcolors.ENDC)
    guess = input("Y/N?\n")
    guess = guess.lower()
    while guess != "y" and guess != "n":
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "\nUnknown input, please try again." + bcolors.ENDC)
        guess = input()
    if guess == "y":
        return "restart"
    return False


# WWPD? ALGORITHM 

def wwpd(name, question_set, stored_list):

    intro(name)

    match_elems1 = [[question_set[i][0], question_set[i][2]] for i in range(len(question_set))]
    match_elems2 = [[stored_list[i][0], stored_list[i][1]] for i in range(len(stored_list))]

    restart = str(match_elems1)[1:-1] in str(match_elems2) and options() == "restart"

    done = False
    for i in question_set:
        group = [i[0], i[2], i[3], True]
        if group not in stored_list or restart:
            done = True 
            if i[1]:
                print(i[1])
            if i[2]:
                print(i[2])
            guess = input()
            while guess != i[3]:
                guess = repeat()
            if str(match_elems1)[1:] not in str(match_elems2):
                op = open("tests/wwpd_storage.py", "w")
                if not stored_list:
                    stored_list = [group]
                else:
                    for j in range(len(stored_list)):
                        if group[0] < stored_list[j][0]:
                            stored_list.insert(j, group)
                            break
                    stored_list.append(group)
                op.write("wwpd_storage = " + str(stored_list))
                op.close()
    if done:
        complete()


# REFERENCE FUNCTIONS

def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25


def how_big(x):
    if x > 10:
        print("huge")
    elif x > 5:
        print("big")
    elif x > 0:
        print("small")
    else:
        print("nothing")

def short_loop_1():
    n = 3
    while n >= 0:
        n -= 1
        print(n)

def short_loop_2():
    positive = 28
    while positive:
        print("positive")
        positive -= 3

def short_loop_3():
    positive = -9
    negative = -12
    while negative:
        if positive:
            print(negative)
        positive += 3
        negative += 3

def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print("foo")

def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make

def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0


# QUESTION SET - ELEMENT FORMAT: [<QUESTION #>, <INITIAL PRINTS> (usually empty), <QUESTION>, <ANSWER>, <COMPLETE?>]
# INSPECT MODULE - convert function body into String: https://docs.python.org/3/library/inspect.html 

booleans_qs = [
    ["", ">>> True and 13", str(True and 13)], 
    ["", ">>> False or 0", str(False or 0)], 
    ["", ">>> not 10", str(not 10)], 
    ["", ">>> not None", str(not None)], 
    ["", ">>> True and 1 / 0 and False", "error"], 
    ["", ">>> True or 1 / 0 or False", str(True or 1 / 0 or False)], 
    ["", ">>> True or 0", str(True or 0)], 
    ["", ">>> False or 1", str(False or 1)], 
    ["", ">>> 1 and 3 and 6 and 10 and 15", str(1 and 3 and 6 and 10 and 15)], 
    ["", ">>> -1 and 1 > 0", str(-1 and 1 > 0)], 
    ["", ">>> 0 or False or 2 or 1 / 0", str(0 or False or 2 or 1 / 0)], 
    ["", ">>> not 0", str(not 0)], 
    ["", ">>> (1 + 1) and 1", str((1 + 1) and 1)], 
    ["", ">>> 1/0 or True", "error"], 
    ["", ">>> (True or False) and False", str((True or False) and False)]
    ]
booleans_qs = [[i + 1] + booleans_qs[i] + [False] for i in range(len(booleans_qs))]

control_qs = [
    ["\n" + inspect.getsource(xk), ">>> xk(10, 10)", str(xk(10, 10))], 
    ["", ">>> xk(10, 6)", str(xk(10, 6))], 
    ["", ">>> xk(4, 6)", str(xk(4, 6))], 
    ["", ">>> xk(0, 0)", str(xk(0, 0))], 
    ["\n" + inspect.getsource(how_big), ">>> how_big(7)", "big"],
    ["", ">>> how_big(12)", "huge"], 
    ["", ">>> how_big(1)", "small"], 
    ["", ">>> how_big(-1)", "nothing"], 
    ["\n" + inspect.getsource(short_loop_1), ">>> short_loop_1()", "2"], 
    ["", "", "1"], 
    ["", "", "0"], 
    ["\n" + inspect.getsource(short_loop_2), ">>> short_loop_2()", "infinite loop"], 
    ["\n" + inspect.getsource(short_loop_3), ">>> short_loop_3()", "-12"],
    ["", "", "-9"], 
    ["", "", "-6"]
    ]
control_qs = [[i + 1] + control_qs[i] + [False] for i in range(len(control_qs))]

what_if_qs = [
    [inspect.getsource(ab), ">>> ab(10, 20)", str(xk(10, 10)), "10"], 
    ["", "", "foo"], 
    [inspect.getsource(bake), ">>> bake(0, 29)", "1"], 
    ["", "", "29"], 
    ["", "", "29"],
    ["", ">>> bake(1, 'mashed potatoes')", "mashed potatoes"], 
    ["", "", "'mashed potatoes'"], 
    ]
what_if_qs = [[i + 1] + what_if_qs[i] + [False] for i in range(len(what_if_qs))]

case_conundrum_qs = [
    [inspect.getsource(special_case), ">>> special_case()", str(special_case())],
    [inspect.getsource(just_in_case), ">>> just_in_case()", str(just_in_case())],
    [inspect.getsource(case_in_point), ">>> case_in_point()", str(case_in_point())]
    ]
case_conundrum_qs = [[i + 1] + case_conundrum_qs[i] + [False] for i in range(len(case_conundrum_qs))]

square_so_slow_qs = [
    [inspect.getsource(square) + "\n" + inspect.getsource(so_slow), ">>> square(so_slow(5))", "infinite loop"]
    ]
square_so_slow_qs = [[i + 1] + square_so_slow_qs[i] + [False] for i in range(len(square_so_slow_qs))]


# WWPD? QUESTIONS

def wwpd_booleans():  
    wwpd("Booleans", booleans_qs, st)

def wwpd_control():  
    wwpd("Control", control_qs, st)

def wwpd_what_if():  
    wwpd("What If?", what_if_qs, st)

def wwpd_case_conundrum():  
    wwpd("Case Conundrum", case_conundrum_qs, st)

def wwpd_square_so_slow():  # wwpd_square_so_slow
    wwpd("Square So Slow", square_so_slow_qs, st)