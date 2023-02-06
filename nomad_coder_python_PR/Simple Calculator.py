# Goal = make calculator without error(+, -, /, *, **)

# def plus(a = "You missing something. Try again", b = "Hmmmmm, nothing to calculate. Try again"):
#   print(a + b)

# def minus(a, b = "Hmmmmm, nothing to calculate. Try again"):
#   print(a - b)

# def divide(a, b = "Hmmmmm, nothing to calculate. Try again"):
#   print(a / b)

# def multiple(a, b = "Hmmmmm, nothing to calculate. Try again"):
#   print(a * b)

# def square(a, b = "Hmmmmm, nothing to calculate. Try again"):
#   print(a ** b)

# plus()
Warning = "Hmmmmm, nothing to calculate. Try again with number and sign [plus => +, minus => -, divide=> /, multiple => *, square=> **] ex) a, \"+\" , b "

num_1 = int(input("First number"))
num_2 = int(input("Second number")) 
how = input("How?")


def calc(a=Warning, how=Warning, b=Warning):

  #기호가 무엇인지 파악
  if how == "":
    print(Warning)

  elif how == "+":
    print(a + b)

  elif how == "-":
    print(a - b)

  elif how == "*":
    print(a * b)

  elif how == "**":
    print(a**b)

  # 아무런 기호가 없거나 위에 상황이 아닐때
  else:
    print(Warning)


calc(num_1, how, num_2)
