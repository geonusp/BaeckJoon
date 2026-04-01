import sys

infi = float('inf')

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0

s_price = sorted(price)

for i in range(len(dist)) :
    # 처음이라 특수 
    if i == 0 :
        answer += dist[0] * price[0]
        continue

    # 마지막도 특수 
    current = price.pop()
    s_price.remove(current)
    
    

    answer += dist[i] * s_price[0]

print(answer)
        
    



