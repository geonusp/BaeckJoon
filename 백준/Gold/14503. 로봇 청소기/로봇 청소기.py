import sys

def input():
    return sys.stdin.readline().rstrip()

# 행 열 
N, M = map(int, input().split())

# 시작 좌표(r,c), 방향 (0:북, 1:동, 2:남, 3:서)
r, c, d = map(int, input().split())

table = []

for _ in range(N) :
    line = list(map(int, input().split()))
    table.append(line)

# 최대 2500 이라 연산 널널하므로 완탐 가능 

dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 처음 위치 청소 
table[r][c] = 2

count = 1

while True :

    moved = False

    # 4방향 
    for _ in range(4) :

        nd = (d+3) % 4

        nr = r + dr[nd]

        nc = c + dc[nd]

        # 방향 갱신 
        d = nd

        # 범위 확인 및 벽인지 확인 
        if 0 <= nr < N and 0 <= nc < M and table[nr][nc] != 1 and table[nr][nc] == 0 :
            count += 1
            table[nr][nc] = 2 # 2는 청소했다는 뜻 
            moved = True # 중첩 반복문으로 인한 플래그 
            r = nr
            c = nc
            break
    
    if moved == True :
        continue

    # 주변 4칸중 모두 청소할 곳 없을때 
    # 4방향 모두 방향갱신되면 원래방향이라 d 갱신 할 필요없음 
    rd = (d+2) % 4

    rr = r + dr[rd]
    rc = c + dc[rd]

    if 0 <= rr < N and 0 <= rc < M and table[rr][rc] != 1 : # 후진할 곳있을때 
        r = rr 
        c = rc

    else :
        break



print(count)