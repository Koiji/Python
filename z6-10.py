print ("Задание 6: Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь")

import math #написал Import вместо import

AB = input("Введите длину первого катета: ")
AC = input("Введите длину второго катета: ")

AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB**2 + AC**2)

S = (AB * AC) / 2

print("Площадь треугольника: %.2f" % S)
print("Гипотенуза треугольника: %.2f" % BC)

######################################################################

print ("Задание 7: Смешано v1 литров воды температуры t1 с v2 литрами воды температуры t2. Найти объем и температуру образовавшейся смеси")

v1 = input("Введите объем первой жидкости: ")
t1 = input("Введите температуру первой жидкости: ")

v1 = float(v1)
t1 = float(t1)

v2 = input("Введите объем второй жидкости: ")
t2 = input("Введите температуру второй жидкости: ")

v2 = float(v2)
t2 = float(t2)

tc = (v1 * t1 + v2 * t2) / (v1 + v2)
vc = v1 + v2

print("Итоговый объем: %.2f" % vc)
print("Итоговая теспература: %.2f" % tc)

######################################################################

print ("Задание 8: Определить периметр правильного n-угольника, описаного около окружности радиуса r")

r = input ("Введите радиус окружности: ")
n = input ("Введите количество стоврон: ")

r = float(r)
n = int(n)

pi = 3.14

a = (2 * r * math.tan(pi/n))

per = a * n

print("Периметр: %.2f" % per)

#####################################################################

print ("Задание 9: Три сопротивления R1, R2, R3 соединены паралельно. Найти сопротивление соединения")

r1 = input ("Введите первое сопротивление: ")
r2 = input ("Введите второе сопротивление: ")
r3 = input ("Введите третье сопротивление: ")

r1 = int(r1)
r2 = int(r2)
r3 = int(r3)

l = (1/r1+1/r2+1/r3)

r = 1 / l

print("Общее сопротивление: %.2f" % r)

#####################################################################

print ("Задание 10: Определить время падения камня на поверхность земли с высоты h")

g = 9.81

h = input ("Введите высоту: ")

h = float(h)

t = math.sqrt(2*h/g)

print("Время падения: %.2f" % t)

input ("Нажмите ENTER для выхода!")