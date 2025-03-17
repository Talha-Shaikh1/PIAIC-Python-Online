'''
The integer numbers (e.g. 2, 4, 20) have type int, the ones with a fractional part (e.g. 5.0, 1.6) have type float.
python have also complex numbers, but we will not discuss them here.
'''

# A complex number has an real part and an imaginary part
z = 3.0 - 2.0j
print(z)
print(z.real)
print(z.imag)

'''
Output:
(3-2j)
3.0
2.0
'''

a = 4 # type int
b = 5.0 # type float
print(a + b)

'''
Division (/) always returns a float. To do floor division and get an integer result you can use the // operator; to calculate the remainder you can use %:
'''
print(17 / 3) # classic division returns a float
print(17 // 3) # floor division discards the fractional part
print(17 % 3) # the % operator returns the remainder of the division
print(5 * 3 + 2) # result * divisor + remainder

'''
With Python, it is possible to use the ** operator to calculate powers:
'''
print(5 ** 2) # 5 squared
print(2 ** 7) # 2 to the power of 7

'''
The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:
'''
width = 20
height = 5 * 9
print(width * height)

'''
If a variable is not “defined” (assigned a value), trying to use it will give you an error:
'''
#print(n) # try to access an undefined variable

'''
There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:
'''

print(4 * 3.75 - 1)

'''
In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator you can type expressions like 2 + 2 in interactive mode and have the result printed. 
'''
tax = 12.5 / 100
price = 100.50
print(price * tax)
# print(price + _)

