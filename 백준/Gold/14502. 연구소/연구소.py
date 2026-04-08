import sys

import copy

from collections import deque
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def bfs(start, N, M, table) :

    r, c = start

    global visited

    table[r][c] = 2

    deq = deque([(r,c)])

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]



    while deq :

        r, c = deq.popleft() 

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]

            # 테이블로 어차피 방문표시할거라 
            if 0 <= nr < N and 0 <= nc < M and table[nr][nc] == 0 :
                visited[nr][nc] = True
                deq.append((nr,nc))
                table[nr][nc] = 2
    return table

# 행 열 
N, M = map(int, input().split())

table = []

for _ in range(N) :
    line = list(map(int, input().split()))
    table.append(line)

table_init = copy.deepcopy(table)  # 초기테이블 저장

# N, M 이 최대 8이라 널널한 편 
# 64P3 (x) 64C3 (o)
# 탐색 시간 
# 퍼지는 시간 (dfs 나 bfs) (N^^2)

visited = [[False] * M for _ in range(N)]

# 0~N 0~M
walls = []
for i in range(N) :
    for j in range(M) :
        if table[i][j] == 0 :
            walls.append((i,j))

wall_c = list(combinations(walls, 3))

candi = -1

for w1,w2,w3 in wall_c :

    count = 0

    # 벽세우기 
    if table[w1[0]][w1[1]] == 0 and table[w2[0]][w2[1]] == 0 and table[w3[0]][w3[1]] == 0 :
        table[w1[0]][w1[1]] = 1
        table[w2[0]][w2[1]] = 1
        table[w3[0]][w3[1]] = 1 

    # 바이러스 퍼트리기 
    for i in range(N) :
        for j in range(M) :
            if visited[i][j] == False and table[i][j] == 2 :
                visited[i][j] = True
                table = bfs((i,j), N,M,table)


    # 안전영역 개수세서 candi리스트에다가 넣어두기 
    for i in range(N) :
        for j in range(M) :
            if table[i][j] == 0 :
                count += 1

    # 최솟값 갱신 
    candi = max(count, candi)

    # 백트래킹 
    table = copy.deepcopy(table_init)
    visited = [[False] * M for _ in range(N)]
    
    
print(candi)
