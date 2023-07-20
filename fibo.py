num = int(input("Enter the number of Fibonacci terms to generate: "))

fib = [0, 1]
while len(fib) < num :
    next = fib [-1] + fib [-2]
    fib.append(next)

print("Fibonacci Sequence:", fib)
