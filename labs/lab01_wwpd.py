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



# INCORRECT ANSWER LOOP, INSTRUCTIONS, COMPLETE, OPTIONS

def repeat():
    print("Try again:")
    return input()

def intro(name):
    print("\nWhat Would Python Display?: " + name)
    print("Type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed.\n")

def complete():
    print_success("All questions for this question set complete.")

def options():
    print_message("All questions for this question set complete. Restart question set?")
    guess = input("Y/N?\n")
    guess = guess.lower()
    while guess != "y" and guess != "n":
        print_error("Unknown input, please try again.")
        guess = input()
    if guess == "y":
        return "restart"
    return False


# WWPD? ALGORITHM 

def wwpd(name, question_set, stored_list):

    intro(name)

    matched = str([i[:-1] for i in question_set])[1:-1] in str([i[:-1] for i in stored_list])
    restart = matched and options() == "restart"
    done = False

    for q in question_set:
        q[4] = True
        if q not in stored_list or restart:
            done = True 
            if q[1]:
                print(q[1])
            if q[2]:
                print(q[2])
            guess = input()
            while guess != q[3]:
                guess = repeat()
            if not matched:
                op = open("tests/wwpd_storage.py", "w")
                for j in range(len(stored_list)):
                    if q[0] < stored_list[j][0]:
                        stored_list.insert(j, q)
                        break
                if q not in stored_list: 
                    stored_list.append(q)
                op.write("wwpd_storage = " + str(stored_list))
                op.close()
    if done:
        complete()


# REFERENCE FUNCTIONS, CLASSES, METHODS, SEQUENCES, ETC.

# https://inst.eecs.berkeley.edu/~cs61a/su22/lab/lab01/

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


# https://inst.eecs.berkeley.edu/~cs61a/su22/disc/disc01/#q1-case-conundrum

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


# QUESTION SET - ELEMENT FORMAT: [<QUESTION NUMBER>, <INITIAL PRINTS> (usually empty), <QUESTION>, <ANSWER>]
# INSPECT MODULE - convert function body into String: https://docs.python.org/3/library/inspect.html 

booleans_qs = [
    [1, "", ">>> True and 13", str(True and 13)], 
    [2, "", ">>> False or 0", str(False or 0)], 
    [3, "", ">>> not 10", str(not 10)], 
    [4, "", ">>> not None", str(not None)], 
    [5, "", ">>> True and 1 / 0 and False", "error"], 
    [6, "", ">>> True or 1 / 0 or False", str(True or 1 / 0 or False)], 
    [7, "", ">>> True or 0", str(True or 0)], 
    [8, "", ">>> False or 1", str(False or 1)], 
    [9, "", ">>> 1 and 3 and 6 and 10 and 15", str(1 and 3 and 6 and 10 and 15)], 
    [10, "", ">>> -1 and 1 > 0", str(-1 and 1 > 0)], 
    [11, "", ">>> 0 or False or 2 or 1 / 0", str(0 or False or 2 or 1 / 0)], 
    [12, "", ">>> not 0", str(not 0)], 
    [13, "", ">>> (1 + 1) and 1", str((1 + 1) and 1)], 
    [14, "", ">>> 1/0 or True", "error"], 
    [15, "", ">>> (True or False) and False", str((True or False) and False)]
]

control_qs = [
    [16, "\n" + inspect.getsource(xk), ">>> xk(10, 10)", str(xk(10, 10))], 
    [17, "", ">>> xk(10, 6)", str(xk(10, 6))], 
    [18, "", ">>> xk(4, 6)", str(xk(4, 6))], 
    [19, "", ">>> xk(0, 0)", str(xk(0, 0))], 
    [20, "\n" + inspect.getsource(how_big), ">>> how_big(7)", "big"],
    [21, "", ">>> how_big(12)", "huge"], 
    [22, "", ">>> how_big(1)", "small"], 
    [23, "", ">>> how_big(-1)", "nothing"], 
    [24, "\n" + inspect.getsource(short_loop_1), ">>> short_loop_1()", "2"], 
    [25, "", "", "1"], 
    [26, "", "", "0"], 
    [27, "\n" + inspect.getsource(short_loop_2), ">>> short_loop_2()", "infinite loop"], 
    [28, "\n" + inspect.getsource(short_loop_3), ">>> short_loop_3()", "-12"],
    [29, "", "", "-9"], 
    [30, "", "", "-6"]
]

what_if_qs = [
    [31, inspect.getsource(ab), ">>> ab(10, 20)", "10"], 
    [32, "", "", "foo"], 
    [33, inspect.getsource(bake), ">>> bake(0, 29)", "1"], 
    [34, "", "", "29"], 
    [35, "", "", "29"],
    [36, "", ">>> bake(1, 'mashed potatoes')", "mashed potatoes"], 
    [37, "", "", "'mashed potatoes'"], 
]

case_conundrum_qs = [
    [38, inspect.getsource(special_case), ">>> special_case()", str(special_case())],
    [39, inspect.getsource(just_in_case), ">>> just_in_case()", str(just_in_case())],
    [40, inspect.getsource(case_in_point), ">>> case_in_point()", str(case_in_point())]
]

square_so_slow_qs = [
    [41, inspect.getsource(square) + "\n" + inspect.getsource(so_slow), ">>> square(so_slow(5))", "infinite loop"]
]

all_qs = [booleans_qs, control_qs, what_if_qs, case_conundrum_qs, square_so_slow_qs]

for set in all_qs:
    for q in set:
        q.append(False)


# WWPD? QUESTIONS

def wwpd_booleans():  
    wwpd("Booleans", booleans_qs, st)

def wwpd_control():  
    wwpd("Control", control_qs, st)

def wwpd_what_if():  
    wwpd("What If?", what_if_qs, st)

def wwpd_case_conundrum():  
    wwpd("Case Conundrum", case_conundrum_qs, st)

def wwpd_square_so_slow():
    wwpd("Square So Slow", square_so_slow_qs, st)