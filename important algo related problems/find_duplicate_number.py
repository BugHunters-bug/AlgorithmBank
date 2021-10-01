input_arr=list(map(int,input().strip().split()))
frequency=dict()
count=1
for i in input_arr:
    if i in frequency:
        frequency[i]=count+1
    else:
        frequency[i]=count

for k,v in frequency.items():
    if v==2:
        print(k)
        break