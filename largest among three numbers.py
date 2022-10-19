a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))

l=0

if a>b and a>c:
    l=a
if b>a and b>c:
    l=b
if c > a and c > b:
    l= c
print(l, "is the largest of three numbers.")