import sys

def input():
    return sys.stdin.readline().rstrip()

positive_inf = float('inf')


n, k = map(int, input().split())

coin_list = []

for _ in range(n) :
    line = int(input())
    coin_list.append(line)


dp = [positive_inf] * (k+1)

dp[0] = 0

for won in range (0,k+1) :

    if dp[won] != positive_inf :
        continue


    for coin in (coin_list) :

        if (won - coin) >= 0 :
            temp = dp[won-coin] + 1
            
            if temp < dp[won] :
                dp[won] = temp


res = dp[k]

if res == positive_inf :
    print(-1)

else :
    print(res)