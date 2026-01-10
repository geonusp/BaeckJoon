import sys 

def input():
    return sys.stdin.readline().rstrip()


N, K = map(int,input().split())

burden = {}

for index in range(1,N+1) :
    line = list(map(int, input().split()))
    burden[index] = line

dp = [[0] * (K+1)  for _ in range (N+1)]


for i in range(1,N+1) :

    weight = burden[i][0]
    value = burden[i][1]

    for w in range(0,K+1) :

        if w >= weight :
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)

        else :
            dp[i][w] = dp[i-1][w]



print(dp[N][K])
