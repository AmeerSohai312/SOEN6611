def absolute(k):
    if k>=0:
        return k
    else:
        return k*-1
def custom_sqrt(number, epsilon=1e-7):
    guess = number / 2  # Initial guess (can be any reasonable value)
    
    while absolute(guess * guess - number) > epsilon:
        guess = 0.5 * (guess + number / guess)

    return guess

def sd(a):
    n=len(a)
    ms=0
    for i in range(n):
        ms=ms+a[i]
    mavg=ms/n
    sds=0
    for i in range(n):
        tv=(a[i]-mavg)*(a[i]-mavg)  
        sds=sds+tv
    
    sdavg=sds/n
    return (custom_sqrt(sdavg))

a=[10, 12, 23, 23, 16, 23, 21, 16]
print(sd(a))