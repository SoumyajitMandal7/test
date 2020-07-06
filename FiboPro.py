fibo_cache={}
def fibo(n):
    if n in fibo_cache:
        return fibo_cache[n]
    
    if n==1:
        val= 1
    elif n==2:
        val= 1
    elif n>2:
        val= fibo(n-1)+fibo(n-2)    
    fibo_cache[n]=val
    return val
for n in range(1,101):
    print(n,":",fibo(n))

    
        