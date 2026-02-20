import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

min_heap = []

for _ in range(N) :
    
    line = int(input())
    heapq.heappush(min_heap, line)

ans = 0

if len(min_heap) >= 2 : 
    while len(min_heap) >= 2 :
        res = 0
        num1 = heapq.heappop(min_heap)
        num2 = heapq.heappop(min_heap)

        res += (num1 + num2)
        ans += res
        heapq.heappush(min_heap, res)

    

print(ans)