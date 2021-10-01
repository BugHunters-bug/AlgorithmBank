# Armstrong number is a number that is equal to the sum of digits raised to the length of the number.
# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
# Write a program to check if the given number is Armstrong or not.
# 153 = (1 ** 3) + (5 ** 3) + (3 ** 3) --- length = 3

# Approach 1
def isArmstrong_str(number: int) -> bool:
    numList = list(map(int, list(str(number))))
    exp = len(numList)
    return number == sum(map(lambda x: x**exp, numList))

# Approach 2
def isArmstrong(number: int) -> bool:
    summ = 0
    num = number
    exp = 0
    while num:
        num //= 10
        exp += 1
    num = number
    while num:
        unit = num % 10
        num //= 10
        summ += unit ** exp
        
    return summ == number

number = 1634
print(isArmstrong(number))