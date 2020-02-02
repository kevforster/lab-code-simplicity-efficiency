"""
Tthis is a dumb calculator that can a
dd and subtract whole numbers from 0-5.
When you run the code, you are prompted to enter 2 numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('WWelcome to this calculator!')
print('It can add and subtract whole numbers from 1 to 5')
a = input('Please choose your first number (0-5): ')
b = input('What do you want to do? minus or plus? (+ or -): ')
c = input('Please choose your second number (0-5): ')

def calculator (a, b, c):
    if b=="+":
        result=int(a) + int(c)
    elif b=="-":
        result=int(a) - int(c)
    print(f"{a} {b} {c} = {result}")

if int(a) > 5 or int(a)<0 or int(c)>5 or int(c)<0 or b!=("-" or "+"):
    print("I am not able to answer this question. Check your input.")
else:
    calculator (a,b,c)

    
print("Thanks for using this calculator, goodbye :)")
