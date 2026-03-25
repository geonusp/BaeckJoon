import sys

import math

def input():
    return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())


entire_prob = math.comb(N, M)

yeo = math.comb(N-M, M) / entire_prob

for i in range(1,K) :
    yeo += math.comb(M, i) * math.comb(N-M, M-i) / entire_prob

ans = 1 - yeo

print(ans)
