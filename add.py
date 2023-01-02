# Program to add nos
a = int(input())
b = int(input())

def addint(*args):
    s=0
    for i in args:
        if type(i) is int:
            s+=i
    return s

print(addint(a,b))
