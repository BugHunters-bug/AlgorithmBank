'''
Old database hashfunction.
Source:
https://en.wikipedia.org/wiki/Adler-32
https://www.youtube.com/watch?v=BWqH4O7OuyY
'''

def adler32(input_plain_text):
    A = 1
    B = 0
    m = 65521
    for char in input_plain_text:
        A = (A + ord(char)) % m
        B = (B + A) % m
    hash = (B << 16) | A
    return hash


