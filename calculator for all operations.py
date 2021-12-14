print("Welcome : Use operators +, - ,/ and * only Enjoy!")
num1 = float(input("Hello Input your first number: "))
operator = input(" Input your operator: ")
num2 = float(input(" Input your second number: "))


if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("Incorrect operator")
