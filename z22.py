print("Задание 22 Найти площадь равнобочной трапеции с основаниями а и Ь и углом а при большем основании а. ")
import math
a=float(input("Введите длину большего основания а: "))
b=float(input("Введите длину меньшего основания b: "))
S=float(input("Введите угол при большем основании в градусах: "))
S=S*math.pi/180
print("Площадь трапеции равна ",(a**2-b**2)/4*math.tan(S))