import sys
n = int(sys.stdin.readline())

a = [-1 for i in range(n+1)]

for i in range(3, n+1):
    if (i<6): 
        if (i==4): continue
        else: a[i]=1
    elif (a[i-3]==-1 and a[i-5]==-1): continue
    elif (a[i-3]==-1 and a[i-5]!=-1): a[i] = a[i-5]+1
    elif (a[i-5]==-1 and a[i-3]!=-1): a[i] = a[i-3]+1
    else: a[i] = min(a[i-3]+1, a[i-5]+1)
    
print(a[n])