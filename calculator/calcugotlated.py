from art import logo

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply (num1, num2):
    return num1 * num2
def divide (num1, num2):
    return num1 / num2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    should_continue = True
    while should_continue:
        num1 =int(input("enter first number: "))
        op = input("pick an operation: \n + \n - \n * \n / \n ")
        num2 = int(input("enter the next number: "))
        result = 0
        for operation  in operations:
            if operation == op:
                result = operations[operation](num1, num2)
                print(f"result: {num1} {operation} {num2} = {result}")
        should_stop = input(f"type y to continue calculating with {result}, or type n to start a new calculation").lower()
        if should_stop == "y":
            should_continue = True
            result += num2
        else:
            should_continue = False

calculator()
