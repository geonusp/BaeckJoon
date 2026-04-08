import sys

from itertools import combinations
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start, N, M, table) :

    deq = deque([(start)])

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    while deq :

        r, c = deq.popleft()

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and table[nr][nc] == 0 :
                table[nr][nc] = 2
                deq.append((nr,nc))

    return table

# 행 열 
N, M = map(int, input().split())

table = []

for _ in range(N) :
    line = list(map(int, input().split()))
    table.append(line)

# max(64C3 * O(V+E), 64C3 * O(N^2)) 

walls = []

for i in range(N) :
    for j in range(M) :
        if table[i][j] == 0 :
            walls.append((i,j))

c_walls = combinations(walls,3)

ans = -1

table_init = [row[:]for row in table]

# 벽 3개 랜덤으로 뽑아서 순회
for w1,w2,w3 in c_walls :

    count = 0

    # 벽 3개 세우기
    if table[w1[0]][w1[1]] == 0 and table[w2[0]][w2[1]] == 0 and table[w3[0]][w3[1]] == 0 :
        table[w1[0]][w1[1]] = 1
        table[w2[0]][w2[1]] = 1
        table[w3[0]][w3[1]] = 1

    # 바이러스퍼뜨리기 (bfs)
    for i in range(N) :
        for j in range(M) :
            if table[i][j] == 2 : # TODO 최적화 고려 
                table = bfs((i,j), N, M, table)


    # 0인곳 세기
    for i in range(N) :
        for j in range(M) :
            if table[i][j] == 0 :
                count += 1
    # 갱신 
    ans = max(count, ans)
    # 백트래킹
        # 테이블복구
    table = [row[:] for row in table_init]


print(ans)