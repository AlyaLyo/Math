import math
import matplotlib.pyplot as plot
import numpy

def f(x,y):
    return x**2

print("Колличество сторон многоугольника : ")
n = int(input())

mesh = 0.1
x_a, x_b = -100, 100
y_a, y_b = -100, 100
x = numpy.arange(x_a, x_b, mesh)
y = numpy.arange(y_a, y_b, mesh)

x_arr = []
y_arr = []

for i in range (1, n + 1):
    print("x_" + str(i) + " : ")
    x_arr.append(int(input()))
    print("y_" + str(i) + " : ")
    y_arr.append(int(input()))

s = 0
for i in x:
    for j in y:
        x_i = i + ( mesh / 2 )
        y_j = j + ( mesh / 2 )

        in_pol = 0;
        t = n - 1;
        for k in range(0, n):
            if ((y_arr[k] < y_j and y_arr[t] >= y_j or y_arr[t] < y_j and y_arr[k] >= y_j) and (x_arr[k] + (y_j - y_arr[k]) / (y_arr[t] - y_arr[k]) * (x_arr[t] - x_arr[k]) < x_i)) :
                if (in_pol == 0):
                    in_pol = 1
                else:
                    in_pol = 0
            t = k

        s = s + ( f(x_i, y_j) * in_pol * mesh * mesh)
        s = (round(s * 100)) / 100

M = 2 * x_b
err = mesh**2 * M * (x_b - x_a + y_b - y_a)

print("Мелкость разбиения : " + str(mesh))
print("Значение интеграла : " + str(s))
print("Значение ошибки : " + str(err))


