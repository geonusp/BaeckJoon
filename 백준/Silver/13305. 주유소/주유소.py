import sys

infi = float('inf')

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0

price.pop()  # 마지막 보정 

s_price = sorted(price)

m = infi


m = infi

for i in range(len(dist)) :   # O(N)
    # 처음이라 특수 
    if i == 0 :
        answer += dist[0] * price[0]
        m = price[0]
        continue

    
    m = min(m,price[i])
    

    answer += dist[i] * m

print(answer)
        
    



