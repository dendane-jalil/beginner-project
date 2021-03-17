'''
simple calculator program
'''
def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mult(x, y):
    return x*y

def div(x,y):
    return (x/y)

keep_going = True

if __name__ == '__main__':
    while keep_going:
        print("Welcome to calculator v0.1 ,Select operation.")
        print("1.Add", end=' ')
        print("2.Subtract", end=' ')
        print("3.Multiply", end=' ')
        print("4.Divide")

        choice = input('make your choice 1,2,3,4 :   ')
        if choice in ('1', '2', '3', '4'):
            print('please give x and y')
        else:
            print('wrong choice')
            break
        try:
            x = float(input('enter x : '))
            y = float(input('enter y : '))
        except ValueError:
            print('wrong value please enter a float number')
        try:
            if choice == '1':
                print(x, "+", y, "=", add(x, y))
            elif choice == '2':
                print(x, "-", y, '=', sub(x, y))
            elif choice == '3':
                print(x, '*', y, '=', mult(x, y))
            elif choice == '4':
                print(x, '/', y, '=', div(x, y))
        except ZeroDivisionError:
            print('ERROR division by zero')
        except NameError:
            break
        break
