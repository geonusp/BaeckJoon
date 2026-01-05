import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

dp = [0] * (30+1)

dp[0] = 1
dp[1] = 0 
dp[2] = 3


for i in range(3, N+1) :
    
    if i % 2 == 0 :
        dp[i] = 4*dp[i-2] - dp[i-4]



    else : 
        dp[i] = 0


print(dp[N])