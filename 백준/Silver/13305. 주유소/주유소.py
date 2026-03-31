import sys

infi = float('inf')

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0

m = infi  # 최신 최솟값찾아내는 역할(중복제거)

for i in range(len(dist)) :
    # 처음이라 특수 
    if i == 0 :
        answer += dist[0] * price[0]
        continue

    # 마지막도 특수 
    if i != len(dist) - 1 :

        m = min(m,price[i],price[i+1])

    answer += dist[i] * m

print(answer)
        
    



