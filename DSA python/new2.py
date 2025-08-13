# print("*")
s='*'
# for i in range(1,4):
#     print(s*i)
# for j in range(4,0,-1):
#     print(s*j)
w=" "
n=4
# for i in range(1,n+1,2):
#     for j in range(1,i+1):
#         print(s,end="")
#     print()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print(s*(i*2-1))

for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print(s*(i*2-1)) 
    