L=[2,3,4,2,20,10,"s","ab",4,"ab","s","s"]
freq=dict()
for i in L:
    count =L.count(i)
    freq[i]=count
print(freq)
