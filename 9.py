from NUMBER import PALINDROME, SPECIAL

# for palindrome
def palindrome_list():
    numbers = eval(input("enter the numbers (num1, num2,...): "))

    palins = []

    for num in numbers:
        if PALINDROME(num) == 1:
            palins.append(num)

    if palins:
        print("palindromes are: ", palins)
    else:
        print("no palindromes")

# for special()

def special_list(limit1, limit2):
    special_list = []
    for num in range(limit1, limit2 + 1):
        if SPECIAL(num) == 1:
            special_list.append(num)
    if special_list:
        print("Special numbers are: ", special_list)
    else:
        print('no special numbers.')

options = """
            1. palindrome
            2. special
            
            enter your option: """

while True:
    opt = eval(input(options))
    if opt == 1:
        palindrome_list()
    elif opt == 2:
        limits = eval(input('enter limits (limit1, limit2): '))
        special_list(limits[0], limits[1])
    else:
        print('Invalid option.')