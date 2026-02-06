import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(start, row, col, table) :

    visited = [[False] * col for _ in range(row)]

    melt_count = 0

    deq = deque([(start)])

    while deq :

        current = deq.popleft()

        r, c = current

        if table[r][c] == 0 :

            for i in range(4) :
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < row and 0 <= nc < col and table[nr][nc] == 1 and visited[nr][nc] == False : # 치즈면 녹인다(방문체크만 하고 더이상 탐색x)
                    table[nr][nc] = 0
                    visited[nr][nc] = True
                    melt_count += 1
                
                elif 0 <= nr < row and 0 <= nc < col and table[nr][nc] == 0 and visited[nr][nc] == False : # 공기면 계속 탐색 
                    deq.append(((nr,nc)))
                    visited[nr][nc] = True

    return melt_count


row, col = map(int, input().split())


table = []

# 테이블 세팅
for _ in range(row) :
    
    line = list(map(int, input().split()))
    table.append(line)

quantity_list = []

day = 0

while True :

    quantity = 0

    visited = [[False] * col for _ in range(row)]
    
    quantity += bfs((0,0), row, col, table)
    
    quantity_list.append(quantity)  

    day += 1

    if quantity_list[-1] == 0 :
        break



print(day-1)
print(quantity_list[day-2])
