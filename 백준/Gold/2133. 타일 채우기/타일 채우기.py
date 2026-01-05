import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

dp = [-1] * (N+1)

dp[0] = 1 
dp[1] = 0
if N > 1 : dp[2] = 3

if N >= 3 :
    
    for i in range(3,N+1) :

        if i % 2 == 0 :
            result = 0
            result += 3 * dp[i-2]
            for j in range(2,(i//2)+1,1):
                result += 2*dp[i-2*(j)]

            dp[i] = result

        elif i % 2 != 0 :
            dp[i] = 0

print(dp[N]) 