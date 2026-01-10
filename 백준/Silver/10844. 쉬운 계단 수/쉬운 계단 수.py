import sys

def input() :
    return sys.stdin.readline().rstrip()

N = int(input())

dp = [[0] * 10 for _ in range(N+1)]

number = 1000000000

for temp in range(1,10) :
    dp[1][temp] = 1

for i in range(2,N+1) :

    for j in range(0,10) :
        if j == 0 : dp[i][j] = dp[i-1][1]
        elif j == 9 : dp[i][j] = dp[i-1][8]
        else : dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

res = 0

for k in range(0,10) :
    res += dp[N][k]


print(res%number)