from random import randint
import sys

def magic_square(a, total):
    if(total % 3 == 0):
        continue
    else:
        total  %= 3
    b = randint(1, total - a)
    c = total - b - a
    d = (-2*a + b + 4*c)//3
    e = (a + b + c)//3
    f = (4*a + b - 2*c)//3
    g = (2*a + 2*b - c)//3
    h = (2*a - b + 2*c)//3
    i = (-a + 2*b + 2*c)//3

    print(a,b,c)
    print(d,e,f)
    print(g,h,i)

val = int(input('Enter a value for the magic square --> '))
total = int(input('Enter the total value for the magic square ---> '))
magic_square(val, total)

    
    
