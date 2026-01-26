import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())



rope_list = []

for _ in range(N) :
    line = int(input())
    rope_list.append(line)

sorted_rope_list = sorted(rope_list, reverse=True)

length = len(rope_list)

dp = [0] * (length+1)

dp[0] = sorted_rope_list[0]

res = dp[0]

for i in range(1,length) :

    dp[i] = sorted_rope_list[i] * (i+1)
    
    if dp[i] > res :
            res = dp[i]


print(res)
