# lab01 wwpd

import inspect

def repeat():
  print("try again:")
  return input()

def intro():
  print("What Would Python Display?")
  print("type the expected output, 'function', 'infinite loop', or 'error'\n")
def outro():
  print("\nall questions for this question set complete")

def xk(c, d):
  if c == 4:
    return 6
  elif d >= 4:
    return 6 + 7 + c
  else:
    return 25

def how_big(x):
  if x > 10:
    print('huge')
  elif x > 5:
    return 'big'
  elif x > 0:
    print('small')
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
    
def wwpd_xk(): # wwpd_xk
  intro()
  
  print(inspect.getsource(xk))

  print(">>> xk(10, 10)")
  x = input()
  while x != str(xk(10, 10)): # 23
    x = repeat()
  
  print(">>> xk(10, 6)")
  x = input()
  while x != str(xk(10, 6)): # 23
    x = repeat()
  
  print(">>> xk(4, 6)")
  x = input()
  while x != str(xk(4, 6)): # 6
    x = repeat()
  
  print(">>> xk(0, 0)")
  x = input()
  while x != str(xk(0, 0)): # 25
    x = repeat()
    
  outro()
  
def wwpd_how_big(): # wwpd_how_big
  intro()

  print(inspect.getsource(how_big))

  print(">>> how_big(7)")
  x = input()
  while x != how_big(7): # big
    x = repeat()
  
  print(">>> how_big(12)")
  x = input()
  while x != how_big(12): # huge
    x = repeat()
  
  print(">>> how_big(1)")
  x = input()
  while x != how_big(1): # small
    x = repeat()
  
  print(">>> how_big(-1)")
  x = input()
  while x != how_big(-1): # nothing
    x = repeat()

  outro()

def wwpd_short_loops(): # wwpd_short_loops
  intro()

  print(inspect.getsource(short_loop_1))
  print(">>> short_loop_one()")
  
  x = input()
  while x != "2":
    x = repeat()
  
  x = input()
  while x != "1":
    x = repeat()
  
  x = input()
  while x != "0":
    x = repeat()

  print("\n" + inspect.getsource(short_loop_2))
  
  print(">>> short_loop_2()")
  x = input()
  while x != "infinite loop":
    x = repeat()

  print("\n" + inspect.getsource(short_loop_3))
  
  print(">>> short_loop_3()")
  x = input()
  while x != "-12":
    x = repeat()
  
  x = input()
  while x != "-9":
    x = repeat()
  
  x = input()
  while x != "-6":
    x = repeat()

  outro()
    
def wwpd_short_booleans(): # wwpd_short_booleans
  intro()
  
  print(">>> True and 13")
  x = input()
  while x != str(True and 13): # 13
    x = repeat()
  
  print(">>> False or 0")
  x = input()
  while x != str(False or 0): # 0
    x = repeat()
  
  print(">>> not 10")
  x = input()
  while x != str(not 10): # False
    x = repeat()
  
  print(">>> not None")
  x = input()
  while x != str(not None): # True
    x = repeat()
  
  print(">>> True and 1 / 0 and False")
  x = input()
  while x != "error":
    x = repeat()
  
  print(">>> True or 1 / 0 or False")
  x = input()
  while x != str(True or 1 / 0 or False): # True
    repeat()
  
  print(">>> True or 0")
  x = input()
  while x != str(True or 0): # True
    x = repeat()
  
  print(">>> False or 1")
  x = input()
  while x != str(False or 1): # 1
    x = repeat()
  
  print(">>> 1 and 3 and 6 and 10 and 15")
  x = input()
  while x != 1 and 3 and 6 and 10 and 15: # 15
    x = repeat()
  
  print(">>> -1 and 1 > 0")
  x = input()
  while x != "True":
    x = repeat()
  
  print(">>> 0 or False or 2 or 1 / 0")
  x = input()
  while x != "2":
    x = repeat()
  
  print(">>> not 0")
  x = input()
  while x != "True":
    x = repeat()
  
  print(">>> (1 + 1) and 1")
  x = input()
  while x != "1":
    x = repeat()
  
  print(">>> 1/0 or True")
  x = input()
  while x != "error":
    x = repeat()
  
  print(">>> (True or False) and False")
  x = input()
  while x != "False":
    x = repeat()

  outro()
  
def wwpd_ab(): # wwpd_ab
  intro()
  
  ab = "\ndef ab(c, d): \n  if c > 5: \n     print(c) \n  elif c > 7: \n      print(d) \n  print('foo')"
  print(f"{ab} \n\n>>> ab(10, 20)")
  x = input()
  while x != "10":
    x = repeat()

  x = input()
  while x != "foo":
    x = repeat()
    
def wwpd_bake(): # bake
  intro()
  
  bake = "def bake(cake, make): \n  if cake == 0: \n    cake = cake + 1 \n    print(cake) \n   if cake == 1: \n    print(make) \n  else: \n    return cake \n  return make"
  print(f"{bake} \n\n>>> bake(0, 29)")
  x = input()
  while x != "1":
    x = repeat()

  x = input()
  while x != "29":
    x = repeat()

  x = input()
  while x != "29":
    x = repeat()


def wwpd_special_case(): # special_case
  special_case = "\ndef special_case(): \n  x = 10 \n  if x > 0: \n    x += 2 \n  elif x < 13: \n    x += 3 \n  elif x % 2 == 1: \n    x += 4 \n  return x"
  print(f"{special_case} \n\n>>> special_case()")
  x = input()
  while x != "12":
    x = repeat()

def wwpd_just_in_case(): # just_in_case
  just_in_case = "def just_in_case(): \n  x = 10 \n  if x > 0: \n    x += 2 \n  if x < 13: \n    x += 3 \n  if x % 2 == 1: \n    x += 4 \n  return x"
  print(f"{just_in_case} \n\n>>> just_in_case()")
  x = input()
  while x != "19":
    x = repeat()

def wwpd_case_in_point(): # case_in_point
  case_in_point = "def case_in_point(): \n  x = 10 \n  if x > 0: \n    return x + 2 \n  if x < 13: \n    return x + 3 \n  if x % 2 == 1: \n    return x + 4 \n  return x"
  print(f"{case_in_point} \n\n>>> case_in_point")
  x = input()
  while x != "12":
    x = repeat()

def wwpd_square_so_slow(): # square_so_slow
  square = "def square(x): \n  print('here!') \n  return x * x"
  so_slow = "def so_slow(num): \n  x = num \n  while x > 0: \n    x = x + 1 \n  return x / 0"
  print(f"{square} \n\n{so_slow} \n\n>>> square(so_slow(5))")
  x = input()
  while x != "infinite loop":
    x = repeat()