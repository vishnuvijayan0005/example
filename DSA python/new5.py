nums=[5,7,7,8,8,10,8]
count=0
count1=0
tar=[]
for i in range(0,len(nums)+1):
    
    if (nums[i]==8):
        tar[0]=i-1
 
print(tar)
