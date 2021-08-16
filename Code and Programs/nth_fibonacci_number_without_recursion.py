"""

Calculate the nth Fibonacci number iteratively.
Input: n - the nth number in the Fibonacci sequence.
Output: the nth Fibonacci number.

"""

def fibonacci(n):

    fib_dict = {0:0, 1:1}

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n not in fib_dict:
            for i in range(2, n+1):
                fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]

        return  fib_dict[n]


print(fibonacci(50))
