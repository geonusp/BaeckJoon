import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

pocket = []

for _ in range(N) :
    line = int(input())
    pocket.append(line)

sorted_pocket = sorted(pocket, reverse = True)

temp = 0
ans = 0

for i in range(0,N) :

    if sorted_pocket[i] > K :
        continue

    elif sorted_pocket[i] <= K :
        while temp <= K : 
            temp += sorted_pocket[i]
            ans += 1

        if temp == K :
            break
        
        temp -= sorted_pocket[i]
        ans -= 1


print(ans)

