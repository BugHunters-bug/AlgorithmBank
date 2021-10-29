""" 
    Luhn algorithm or Luhn formula
    Checksum algorithm.
    Source:https://en.wikipedia.org/wiki/Luhn_algorithm

"""

def luhn(input_number):
    
    input_number = [int(i) for i in str(input_number)]
    input_number.reverse()
    
    sum_answer = 0
    for i, number in enumerate(input_number):
        temp = number
        if i % 2 == 0:
            temp = number * 2
        if temp > 9:
            temp -= 9
            
        sum_answer = sum_answer + temp

    return sum_answer % 10 == 0
