#  pyramid builder
# project from a beginner

size = input("Give the size of the pyramid(make sure it is an integer number):  ")
shape = input('Give the character you want: ')
try:
    for i in range(0, int(size)):

        for j in range(0, int(size)-i):
            print(" ", end="")
        for k in range(0, 2*i+1):
            print(f'{shape}', end="")
        print("", end="\n")
except:
    print("wrong input ")


