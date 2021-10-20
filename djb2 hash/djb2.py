'''
Old hashfunction.

Explaination:
(magic_hash_nr + (magic_hash_nr << 5)) is equivalent to (magic_hash_nr*33). 
This because the bit shift of <<5 is multiplying by 32 then we add another one.

Source:
http://www.cse.yorku.ca/~oz/hash.html
https://stackoverflow.com/questions/1579721/why-are-5381-and-33-so-important-in-the-djb2-algorithm
'''


def djb2(input_plain_text):
    magic_hash_nr = 5381
    for char in input_plain_text:
        magic_hash_nr = ord(char) + (magic_hash_nr + (magic_hash_nr << 5))
    magic_hash_nr = magic_hash_nr & 0xFFFFFFFF
    return magic_hash_nr