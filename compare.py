def compare(arr):
    ans,zero,ones,twos=[],[],[],[]
    for i in arr:
        if i ==0:
            zero.append(i)
        elif i ==1:
            ones.append(i)
        elif i== 2:
            twos.append(i)
    ans=zero+twos+ones
    print(ans)      
    return ans

arr=[0,1,0,2,2,2,1,1,0,0,0,1,2,1,2,0]
compare(arr)