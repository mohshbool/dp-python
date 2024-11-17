import time

def fib_iterative(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    prev = 0
    current = 1
    
    for _ in range(2, n + 1):
        prev, current = current, prev + current
    
    return current

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fib_recursive_dp(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_recursive_dp(n-1, memo) + fib_recursive_dp(n-2, memo)
    return memo[n]

def time_fibonacci(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def calculate_fibonacci(n):
    methods = {
        'Iterative SP': fib_iterative,
        'Recursive SP': fib_recursive,
        'Iterative DP': fib_iterative_dp,
        'Recursive DP': fib_recursive_dp
    }
    
    print(f"\nCalculating {n}th Fibonacci number:")
    print("-" * 50)
    
    for method_name, func in methods.items():
        try:
            result, exec_time = time_fibonacci(func, n)
            print(f"{method_name} -> Result: {result:15} Time: {exec_time:.6f} seconds")
        except RecursionError:
            print(f"{method_name} -> RecursionError: n too large")


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    if n < 0:
        print("Please enter a non-negative number.")
    if n == 1:
        print("The 1st Fibonacci number is 1.")
        print("The program will not run for n <= 1.")

    calculate_fibonacci(n)