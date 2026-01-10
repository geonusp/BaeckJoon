import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())

py = {}

dp = [[0] * (n+1) for _ in range(n+1)]

for index in range(1,n+1) :
    line = list(map(int, input().split()))
    line.insert(0,0)
    py[index] = line



for i in range(1,n+1) :

    for j in range(1,i+1) :
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + py[i][j]


res = max(dp[n])

print(res)