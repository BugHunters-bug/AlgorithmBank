'''
Old database hashfunction.
Source:
https://api.riot-os.org/group__sys__hashes__sdbm.html
http://www.cse.yorku.ca/~oz/hash.html
Docs for ord: https://docs.python.org/3/library/functions.html#ord
Returns the unicode character of a char.
'''


def sdbm(input_plain_text):
    hash_output = 0
    for char in input_plain_text:
        hash_output = ord(char) + (hash_output << 6) + (hash_output << 16) - hash_output
    return hash_output