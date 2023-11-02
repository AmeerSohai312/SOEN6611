def absolute(k):
    if k>=0:
        return k
    else:
        return k*-1

def mad(a):
    n=len(a)
    ms=0
    for i in range(n):
        ms=ms+a[i]
    mavg=ms/n
    mads=0
    for i in range(n):
        mads=mads+(absolute(a[i]-mavg))        
    madavg=mads/n
    
    return madavg
# example run
a=[10, 12, 23, 23, 16, 23, 21, 16]
print(mad(a))
        
        