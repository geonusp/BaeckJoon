import sys

def input():
    return sys.stdin.readline().rstrip()

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# dfs_stack 풀이
def dfs_stack(start_coor, row, col, table, visited):

    r, c = start_coor

    stack = [start_coor]

    count = 0

    while stack :

        coor = stack.pop()

        r, c = coor

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] == False and table[nr][nc] == 0 : # 외부 공기
                visited[nr][nc] = True
                stack.append((nr,nc))

            elif 0 <= nr < row and 0 <= nc < col and visited[nr][nc] == False and table[nr][nc] == 1 : # 치즈 
                visited[nr][nc] = True
                table[nr][nc] = 0
                count += 1
    
    return count

row, col = map(int, input().split())

table = []

for _ in range(row):
    line = list(map(int, input().split()))
    table.append(line)

hour = 0 
count_list = []

while True :
    melting_count = 0 
    hour += 1
    visited = [[False] * col for _ in range(row)]
    melting_count += dfs_stack((0,0), row, col, table, visited)

    if melting_count == 0 :
        break

    count_list.append(melting_count)

print(hour-1)
print(count_list[-1])



