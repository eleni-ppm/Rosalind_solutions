
#with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of  rabbit pairs (instead of only 1 pair)

def fib(n, k):
    if n <= 2:
        return 1
    else:
        return fib(n-1,k) + k * fib(n-2, k)
    
n = 5
k = 3

fib(n,k)

print(fib(int(n), int(k)))