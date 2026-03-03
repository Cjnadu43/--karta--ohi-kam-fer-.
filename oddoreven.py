# num = int(input("enter a number to check! \n"))
#
# if num % 2 == 0:
#     print("It is even")
# elif num % 2 != 0:
#     print("it is odd")
# else:
#     print("please enter a number")

for num in range(1,101):
    if num % 3 == 0:
        print("fizz")
    print(num)
    if num % 5 == 0:
        print("buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    else:
        print(num)








