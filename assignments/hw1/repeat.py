import sys

def repeat(string, n):
    counter = n
    res = ""
    while counter > 0:
        if counter == n:
            res += string.capitalize()
        else:
            res += " " + string.lower()

        counter -= 1

        if counter == 0:
            res += "."

    print(res)
    
if __name__ == "__main__":
    string = str(sys.argv[1])
    n = int(sys.argv[2])
    
    repeat(string, n)