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

res = 0

for target in range(1, k+1) :
    
    for i in range(len(pocket)) :

        
        prev = target - pocket[i]
        
        if prev >= 0 :
            res = memo[prev] + 1

            if res < memo[target] :
                memo[target] = res

if memo[k] == positive_inf :
    print(-1)
else :
    print(memo[k])