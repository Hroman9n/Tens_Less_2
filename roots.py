from math import sqrt


def line_input():   # ввод коэффициентов в одну строку
    coef = list(input("please, enter coefficients in line: ").split()) #

    abc = list(map(int, coef))

    return(abc)

def sep_input():    # ввод коэффициентов по отдельности
    print("please, enter coefficients separately")

    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))

    abc = [a, b, c]

    return(abc)

def a0(abc):    # если а=0 (3х+15=0)
    b = abc[1]
    c = abc[2]

    res = -c/b

    print("корень уравнения x =", res)

def b0(abc):    
    a = abc[0]
    c = abc[2]

    if c < 0:
        res = sqrt(-(c/a))
        print ("Корни квадратного уравнения: х1 = {0}, x2 = {1}".format(res, -res))


def c0(abc):    # если с=0 (2х^2+8х=0)
    a = abc[0]
    b = abc[1]

    res = -b/a

    print("Корни уравнения: х1 = 0, х2 =", res)

def roots(abc): # Стандартная функция вычисления квадратного уравнения
    a = abc[0]
    b = abc[1]
    c = abc[2]

    d = b**2 - 4*a*c
    dsqr = sqrt(d)

    x1 = (-b + dsqr)/(2*a)
    x2 = (-b - dsqr)/(2*a)

    print("Корни квадратного уравнения: х1 = {0}, x2 = {1}".format(x1, x2))


abc= list() # пустой список, в который позже запишутся коэффициенты

mthd = input("are you gonna write coefficients in line (enter line) or separately (enter sep): ")

if mthd == "line":
    abc=line_input()
elif mthd == "sep":
    abc=sep_input()

#print(abc) # проверка работоспособности функций

if abc[0] == 0:
    a0(abc)
elif abc[1] == 0:
    b0(abc)
elif abc[2] == 0:
    c0(abc)
else:
    roots(abc)