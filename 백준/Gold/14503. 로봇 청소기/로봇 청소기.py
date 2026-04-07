import sys

from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def sear(start, N, M):

    r,c,d = start 

    visited = [(r,c)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]


    while True :

        moved = False
            

        for i in range(4) :

            # 반시계 회전
            nd = (d + 3) % 4

            nr = r + dr[nd]
            nc = c + dc[nd]

            d = nd


            #  범위 체크 및 벽 여부
            if 0 <= nr < N and 0 <= nc < M and table[nr][nc] != 1 and (nr,nc) not in visited :
                visited.append((nr,nc))
                r = nr
                c = nc
                d = nd
                moved = True
                break
                
        if moved == True :
            continue
        # 주변 4칸 중 청소 안된 빈칸없으면
        
        # 후진 가능하면 후진
        # d 0
        if d == 0 :
            rr = r + 1
            rc = c
            if 0 <= rr < N and 0 <= rc < M and table[rr][rc] != 1 :
                r = rr
                c = rc
            else : 
                return len(visited)
        # d 1
        elif d == 1 :
            rr = r
            rc = c - 1
            if 0 <= rr < N and 0 <= rc < M and table[rr][rc] != 1 :
                r = rr
                c = rc
            else : 
                return len(visited)
        # d 2
        elif d == 2 :
            rr = r - 1
            rc = c
            if 0 <= rr < N and 0 <= rc < M and table[rr][rc] != 1 :
                r = rr
                c = rc
            else : 
                return len(visited)
        # d 3
        elif d == 3 :
            rr = r
            rc = c + 1
            if 0 <= rr < N and 0 <= rc < M and table[rr][rc] != 1 :
                r = rr
                c = rc
            else : 
                return len(visited)
    
    
    

# 행 열 
N, M = map(int, input().split())

# 시작 좌표(r,c), 방향 (0:북, 1:동, 2:남, 3:서)
start_r, start_c, start_d = map(int, input().split())

table = []

for _ in range(N) :
    line = list(map(int, input().split()))
    table.append(line)

ans = sear((start_r,start_c,start_d), N, M)

print(ans)