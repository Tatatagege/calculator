what=input("What to do: ")
a=float(input("put the first number: "))
b=float(input("put the second number: "))

if what == "+":
    c=a+b
    print("result:" + str(c))
elif what == "-":
    c=a-b
    print("result:" + str(c))
elif what == "*":
    c=a*b
    print("result:" + str(c))
elif what == "/":
    c=a/b
    print("result:" + str(c))
elif what== "**":
    c=a**b
    print("result:" + str(c))
elif what == "%":
    c=a%b
    print("result:" + str(c))
else:
    print("It is wrong")
