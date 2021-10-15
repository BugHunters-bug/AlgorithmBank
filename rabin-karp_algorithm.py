
d = 265
 
# pat  -> pattern
# txt  -> text
# prime -> A prime number
 

def search(pat, txt, prime):

    M = len(pat)

    N = len(txt)
    i = 0
    j = 0
    p = 0    
    t = 0    

    h = 1

    for i in xrange(M-1):

        h = (h*d)%prime
 

    for i in xrange(M):

        p = (d*p + ord(pat[i]))%prime

        t = (d*t + ord(txt[i]))%prime
 

    for i in xrange(N-M+1):

        if p==t:

            for j in xrange(M):

                if txt[i+j] != pat[j]:

                    break

                else: j+=1

            if j==M:

                print "Pattern found at index " + str(i)
 

        if i < N-M:

            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%prime
 

            if t < 0:

                t = t+prime
 


txt = "I AM CHAITANYA"

pat = "AM"
 


prime= 101
 
# Function Call
search(pat,txt, prime)
