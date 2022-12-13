import math
v=int(input("please enter 1 for + - * / and enter 2 for sin cos tan cot fact rad"))
if v==1:
    a = float(input("please enter first number = "))
    b = float(input("please enter second number = "))
    op=input("please enter operation = ")

    if op == "+":
        resault=a+b

    if op == "-":
        resault=a-b

    if op =="/":
        resault=a/b

    if op =="*":
        resault=a*b 
if v==2:
    x = float(input("please enter a number = "))
    if op == "sin":
        resault=math.sin(math.radians(x))           
    if op== "cos":
        resault=math.cos(math.radians(x))
    if op=="tan":
        resault=math.tan(math.radians(x))
    if op=="cot":
        resault=math.cot(math.radians(x))
    if op=="factorial":
        a=int(x)
        resault=math.factorial(x)
    if op=="radical":
        resault=math.sqrt(x)
print(resault)
    