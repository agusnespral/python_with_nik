from math import *

again = 'y'
while again == 'y':

    print('Welcome! This calculator works only with integer numbers')
    first = input('Input first number and press enter:')
    if first.isdigit():
        first = int(first)

    while type(first) != int:
        if type(first) != int:
            first = input('You can only insert integer numbers! Please input first number and press enter:')
            if first.isdigit():
                first = int(first)
        else:
            break

    operation_type = input('Insert type of operation and press enter: \n'
                 'a for addition \n'
                 'b for rest\n'
                 'c or multiply\n'
                 'd for division\n')

    while operation_type != 'a' and operation_type != 'b' and operation_type != 'c' and operation_type != 'd':
        operation_type = input('You inserted an invalid operation type. Please insert type of operation and press enter: \n'
                               'a for addition \n'
                               'b for rest\n'
                               'c or multiply\n'
                               'd for division\n')
    second = input('Input second number and press enter:')
    if second.isdigit():
        second = int(second)

    while type(second) != int:
        if type(second) != int:
            second = input('You can only insert integer numbers! Please input second number and press enter:')
            if second.isdigit():
                second = int(first)
        else:
            break
    def calculator(num1, num2):
        if operation_type == 'a':
            result = num1 + num2
            print ('La suma de ', num1, 'y', num2, 'es igual a =', result)
        elif operation_type == 'b':
            result = num1 - num2
            print ('La resta de ', num1, 'y', num2, 'es igual a =', result)
        elif operation_type == 'c':
            result = num1 * num2
            print ('La multiplicacion de ', num1, 'y', num2, 'es igual a =', result)
        else:
            result = num1 / num2
            print ('La division de ', num1, 'y', num2, 'es igual a =', result)


    print(calculator(first, second))
    again = input('Do you want to do a new operation? y/n')
    if again != 'y' and again != 'n':
        again = input("Please enter a valid answer. 'y' for YES or 'n' for no. Do you want to do a new operation? y/n")