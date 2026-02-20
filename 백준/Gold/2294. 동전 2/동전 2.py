import sys

def input():
    return sys.stdin.readline().rstrip()

positive_inf = float('inf')

n, k = map(int, input().split())

pocket = []

for _ in range(n) :
    line = int(input())
    pocket.append(line)

memo = [positive_inf] * (k+1)

memo[0] = 0

for i in range(1,k+1) :

    for j in range(len(pocket)) :

        prev = i - pocket[j]

        if prev >= 0 :
            temp = memo[prev] + 1

            if temp < memo[i] :
                memo[i] = temp


if memo[k] == positive_inf :
    print(-1)
else :
    print(memo[k])