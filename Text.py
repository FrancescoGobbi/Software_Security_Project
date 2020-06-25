def fib():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

def qualcosa(n):
	if n==1 :
		return 1
	if n==2 :
		return 1

	return qualcosa(n-1) + qualcosa(n-2)

fib_gen = fib()
for _ in range(10):
    next(fib_gen)