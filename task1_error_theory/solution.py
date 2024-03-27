from math import sqrt, cos, cosh
from prettytable import PrettyTable


def fact(x):
	ans = 1
	if x != 0:
		for i in range(1, x + 1): ans *= i
	return ans


def ch(x):
	un = x
	ans = 0
	k = 0
	while abs(un) > 10**(-9):
		un = (x**(2*k)/fact(2*k))
		ans += un
		k += 1
	return ans


def cosinus(x):
	un = x
	ans = 0
	k = 0
	while abs(un) > 10**(-9):
		un = (-1)**k*x**(2*k)/fact(2*k)
		ans += un
		k += 1
	return ans


def sqr(x):
	un = x
	prev = x + 0.5
	k = 0
	while abs(un - prev) > 10**(-9):
		prev = un
		if prev == 0: prev = 0.1
		un = (prev + x/prev) / 2
		k+=1
	return un


def z(x):
	return ch(1 + sqr(1 + x)) * cosinus(sqr(1 + x - x**2))


xs = [0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2]

print(xs)
table = []

a = [(1 + sqr(1+x)) for x in xs]
true_a = [(1 + sqrt(1+x)) for x in xs]
da = [10**(-6)/(4*0.51*2.1) for i in range(len(a))]
true_da = [abs(a[i] - true_a[i]) for i in range(len(a))]

b = [sqr(1+x-x**2) for x in xs]
true_b = [sqrt(1+x-x**2) for x in xs]
db = [10**(-6)/(4*4.13*1.08) for i in range(len(b))]
true_db = [abs(b[i] - true_b[i]) for i in range(len(b))]

fi = [ch(a[i]) for i in range(len(a))]
true_fi = [cosh(a[i]) for i in range(len(a))]
dfi = [10**(-6)/1.02 for i in range(len(a))]
true_dfi = [abs(fi[i]-true_fi[i]) for i in range(len(a))]

psi = [cos(b[i]) for i in range(len(b))]
true_psi = [cos(b[i]) for i in range(len(b))]
dpsi = [10**(-6)/8.26 for i in range(len(b))]
true_dpsi = [abs(psi[i] - true_psi[i]) for i in range(len(b))]

z = [z(x) for x in xs]
true_z = [cosh(1 + sqrt(1+x))*cos(sqrt(1+x-x**2)) for x in xs]
dz = [10**(-6) for i in range(len(z))]
true_dz = [abs(z[i] - true_z[i]) for i in range(len(z))]

print(true_z)

mytable = PrettyTable()
mytable.field_names = ["x", "A", "/\\A", "*A*", "*/\\A*", "B", "/\\B", "*B*", "*/\\B*", "F", "/\\F", "*F*", "*/\\F*", "G", "/\\G", "*G*", "*/\\G*", "Z", "/\\Z", "*Z*", "*/\\Z*"]
t = [xs, a, da, true_a, true_da, b, db, true_b, true_db, fi, dfi, true_fi, true_dfi, psi, dpsi, true_psi, true_dpsi, z, dz, true_z, true_dz]

table = [[round(m[i], 3) for m in t] for i in range(10)]


mytable.add_rows(table)
print(mytable)
