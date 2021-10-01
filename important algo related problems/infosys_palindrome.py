# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def check_palindrome(n):
    str_n=str(n)
    rev_str_n=str_n[::-1]
    # print(rev_str_n)
    if(rev_str_n == str_n):
        return True
    else: return False

n=int(input(""))
str_n=str(n)
rev_n=str_n[::-1]
rev_n_int=int(rev_n)
# print(rev_n_int)
n=n+rev_n_int
while(not check_palindrome(n)):
    str_n=str(n)
    rev_n=str_n[::-1]
    rev_n_int=int(rev_n)
    n=n+rev_n_int
print(n)
    