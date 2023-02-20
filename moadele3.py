import math
import numpy
import cmath


print("Hi wellcome\nformat of Grade 3 equation is like this: \nax3 + bx2 + cx + d = 0")


def grade_3_equation(a, b, c, d):

    b = b / a
    c = c / a
    d = d / a
    a = a / a
    p = c - b**2 / 3
    q = (2 * b**3) - (b * c / 3) + d
    delta = (q**2 / 4) + (p**3 / 27)

    if delta > 0:
        x = math.pow(-q/2 + math.sqrt(delta), 1/3) + \
            cmath.exp(3 * math.log(-q/2 - math.sqrt(delta), 1/3)) - b/3
        print("reshe yeki hast va moadel on barabar ast ba: ", x)

    elif delta == 0:
        x1 = (-2 * math.pow(q/2, 1/3) - b/3)
        x2 = math.pow(q/2, 1/3) - b/3
        print("reshe dota hast va moadel on barabar ast ba: /nx1 =",
              x1, "\nx2 = x3 =", x2)

    else:
        x1 = 2/math.sqrt(3)*math.sqrt(-p)*math.sin((1/3 *
                                                    math.sinh((3*math.sqrt(3)*p) / (2*(math.sqrt(-p)**3))))) - b/3
        x2 = -2/math.sqrt(3)*math.sqrt(-p)*math.sin(1/3*math.sinh((3 *
                                                                   math.sqrt(3)*p) / (2*math.sqrt(-p)**3) + numpy.pi/3)) - b/3
        x3 = 2/math.sqrt(3)*math.sqrt(-p)*math.cos(1/3*math.sinh((3 *
                                                                  math.sqrt(3)*p) / (2*math.sqrt(-p)**3) + numpy.pi/6)) - b/3
        print("reshe dota hast va moadel on barabar ast ba: \nx1 = ",
              x1, "\nx2 = ", x2, "\nx3 = ", x3)


a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
d = float(input("enter d: "))

grade_3_equation(a, b, c, d)
