import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

# 여기서 나오는 최댓값구해서 candi 에 넣어두기 
def bfs(start, table, R, C, visited) :

    # 상 하 좌 우 
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    r, c = start

    count = 0

    deq = deque([(start, count)])

    visited[r][c] = True

    M = -1 

    while deq :


        current, count = deq.popleft()

        # 최댓값 갱신 로직 
        M = max(M, count)

        r,c = current

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]

            # 백트래킹 구현 
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == False and table[nr][nc] == 'L' :
                visited[nr][nc] = True
                deq.append(((nr,nc), count+1))

    return M


R, C = map(int, input().split())

table = []

for _ in range(R) :
    line = input()
    table.append(list(line))


# 최장거리 + 최단거리
candi = [] 
for i in range(R) :
    for j in range(C) :
        if table[i][j] == 'L' :
            visited = [[False] * C for _ in range(R)]
            candi.append(bfs((i,j), table, R, C, visited))
        


print(max(candi))