import math
import matplotlib.pyplot as plot
import numpy

def f(x):
	return pow(3,x)

I = 6 / (numpy.log(3))

a, b = 1, 2
x = numpy.arange(a, b, 0.01);

print("Число точек разбиения : ")
n = int(input())

print("Способ выбора оснащения (1 - левые, 2 - правые, 3 - средние) : ")
xi = int(input())

l = (b - a) / n

if xi == 1 :
	shift = -0.5 * l
	xi = "левые"
elif xi == 2 :
	shift = 0.5 * l
	xi = "правые"
else :
	shift = 0
	xi = "средние"

S = 0
middle = []

x_i = []
for i in range (0, n) :
	x_i.append(a + (i * l))
	middle.append(a + ((i + 0.5) * l))
x_i.append(b)

y_i = []
for i in middle :
	y_i.append(f(i + shift))
	S += f(i + shift) * l

R_n = abs(I - S)

plot.plot(x, f(x),'r')
plot.bar(middle, y_i, width = l, edgecolor = "b")
plot.grid(True)

plot.xlabel(r'$X$')
plot.ylabel(r'$F(X)$')
plot.title("Число точек разбиения : " + str(n) + ". Оснащение : " + xi + ". I : " + str((S)), fontsize = 10 )
plot.text(1.0,8,"Погрешность : " + str(R_n))

plot.savefig("n" + str(n) + "xi" + str(xi) + ".png")
plot.show()

