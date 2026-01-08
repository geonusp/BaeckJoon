import sys

def input():
    return sys.stdin.readline().rstrip()



N = int(input())

m = 1000000007

dp = [0] * (1000000+1)
sp = [0] * (1000000+1)

dp[0] = 1
dp[1] = 2
dp[2] = 7
dp[3] = 22


if N >= 4 :
    for i in range(3,N+1) :

        # dp[i] = 2*dp[i-1] + 3*dp[i-2] + 2*(dp[i-3] + ... + dp[0]) 

        a = ((2 % m) * (dp[i-1] % m)) % m 
        b = ((3 % m) * (dp[i-2] % m)) % m 
        
        multi = (2 % m) * (dp[i-3] % m) % m   # 2*dp[i-3]
        sp[i-3] = ((sp[i-4] % m) + (multi % m)) % m

        dp[i] = ((a % m) + (b % m) + (sp[i-3])) % m

print(dp[N])
