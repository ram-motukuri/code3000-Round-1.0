def shift(n):
    k=[')','!','@','#','$','%','^','&','*','(']
    n=list(str(n))
    p=list(map(lambda i:k[int(i)],n))
    p="".join(p)
    return p
def mem_fib(n, _cache={}):
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n

j=int(input())
ans=""
for i in range(j):
    ans=ans+shift(mem_fib(i))
print(ans[::-1])
