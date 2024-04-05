# fibonocci series from 1-50 
from functools import reduce
n=50
fib_series=lambda n:reduce(lambda x,_:x+[x[-2]+x[-1]],range(n-2),[0,1])
fib_lambda=fib_series(n)
print(fib_lambda)
