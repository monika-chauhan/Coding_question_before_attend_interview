def Fibonacci_series(n):
    dp = [0] * (n+1)
    dp[0] = 0 
    if n > 0:
        dp[1] = 1 
    if n > 1:
        dp[2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
for i in range(10):
    print(Fibonacci_series(i))

