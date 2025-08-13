L=[[24,25.5,89,4],[67,89,10,0],[91,34,23,11]]
totalsum=[]
sum=0
for i in range(0,len(L)):
    for index in range(0,len(L[i])) :
        sum+=L[i][index]
    totalsum.append(sum)
    sum=0
print(totalsum)
reversed=[]
for i in L:
   reversed.append(i[::-1])
print(reversed)
