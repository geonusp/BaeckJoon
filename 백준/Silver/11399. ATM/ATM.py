import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

dp = [0] * (N)

p = list(map(int,input().split()))

sorted_p = sorted(p)

length = len(p)

dp[0] = sorted_p[0]

for i in range(1, length) :
    
    if dp[i] == 0 :
        dp[i] = dp[i-1] + sorted_p[i]
    
    else :
        continue

res = 0

for item in dp :
    res += item

print(res)