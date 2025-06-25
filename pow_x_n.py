def myPow(x: float, n: int):
    if n==0:
        return 1
    if n<0:
        n = abs(n)
        x = 1/x
    if n%2 == 0:
        res = myPow(x*x, n//2)
        return res
    else:
        res = myPow(x*x,n//2)
        return x* res

print(myPow(2,2))