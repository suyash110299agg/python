# def calc(operator):
#     print("enter the operation you wish to perform\n")
#     operator=input("+, -, *, /")
#     if operator == "+":
#        def add(num1, num2):
#             sum=num1+num2
#             return sum
#     if operator == "-":
#        def sub(num1, num2):
#             diff=num1-num2
#             return diff
#     if operator == "*":
#        def mul(num1, num2):
#             prod=num1*num2
#             return prod
#     if operator == "/":
#        def div(num1, num2):
#             quo=num1/num2
#             return quo
    
# num1=int(input())
# num2=int(input())
# print(calc("+"))


def calc():
    print("Enter the operation you wish to perform: +, -, *, /")
    operator = input()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if operator == "+":
        def add(num1, num2):
            sum = num1 + num2
            return sum
        result = add(num1, num2)
    elif operator == "-":
        def sub(num1, num2):
            diff = num1 - num2
            return diff
        result = sub(num1, num2)
    elif operator == "*":
        def mul(num1, num2):
            prod = num1 * num2
            return prod
        result = mul(num1, num2)
    elif operator == "/":
        def div(num1, num2):
            quo = num1 / num2
            return quo
        result = div(num1, num2)
    else:
        print("Invalid operator!")
        return
    
    print("Result:", result)

calc()