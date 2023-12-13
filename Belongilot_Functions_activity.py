print("CS112: COMPUTER PROGRAMMING 1 \nFunctions Activity \nSubmitted by: Clyde Joshua C.Belongilot")

print("Guidelines:\n[1] If the numbers are different then all will be added")
print("[2] If the numbers are all the same, all number will be multiplied")
print("[3] If two numbers are the same, similar numbers will be multiplied and different number will be added")
print("------------------------------------------------------------------------------------------------------")
while True:
    def simvar():
        result = first * second * third
        print(result)

    def difvar():
        result2 = first + second + third
        print(result2)

    first = eval(input("Enter first number:"))
    second = eval(input("Enter second number:"))
    third = eval(input("Enter third number:"))

    if first == second == third:
        simvar()

    elif first == second != third:
        result_1 = first * second + third
        print(result_1)

    elif first == third != second:
        result_2 = first * third + second
        print(result_2)

    elif third == second != first:
        result_3 = third * second + first
        print(result_3)

    elif third != second != first:
        difvar()
