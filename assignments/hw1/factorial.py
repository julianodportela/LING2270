import sys

def factorial(x):
    res = 1
    counter = x
    while counter > 1:
        res *= counter  
        counter -= 1

    print(res)

if __name__ == "__main__":
    x = int(sys.argv[1])
    factorial(x)