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
    for i, num in enumerate(number):
        fact += fac(num)
    if fact == number:
        return 1
    return -1