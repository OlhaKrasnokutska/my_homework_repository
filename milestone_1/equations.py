import math

user_input = input("Enter an equation as a string of the form: `<a>x^2 + <b>x + <c> = 0`: ")
print(user_input)
equation = user_input.replace(' ', '')
print(equation)
eq_split_x2 = equation.split('x^2')
if (eq_split_x2[0] == ''):
    eq_split_x2[0] = 1
a = int(eq_split_x2[0])
eq_split_x = str(eq_split_x2[1]).split('x')
if (eq_split_x[0] == '-'):
    eq_split_x[0] = '-1'
b = int(eq_split_x[0].replace('+', '').replace('(','').replace(')',''))
eq_split_final = eq_split_x[1].split('=')
c = int(eq_split_final[0].replace('+', '').replace('(','').replace(')',''))
print(a, b, c)

d = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(d))/(2 * a)
x2 = (-b - math.sqrt(d))/(2 * a)
print(x1, x2)