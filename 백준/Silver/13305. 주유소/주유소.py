import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())


dist = list(map(int, input().split()))
weight = list(map(int, input().split()))

apply = []

res = 0

for i in range(0,N-1) :
    apply.append(weight[i])
    res += dist[i] * min(apply)


print(res)