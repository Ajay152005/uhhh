def PALINDROME(number):
    number = str(number)
    if number == number[::-1]:
        return 1
    else:
        return -1
    
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    
def SPECIAL(number):
    fact = 0
    numbers = [int(num) for num in str(number)]
    for num in numbers:
        fact += fac(num)
    if fact == number:
        return 1
    return -1