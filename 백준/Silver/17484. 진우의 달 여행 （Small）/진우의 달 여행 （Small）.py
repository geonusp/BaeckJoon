import sys

def input():
    return sys.stdin.readline().rstrip()


def dfs(current, N, M, before_d, candi_list, su):
    
    r, c = current
    
    # 정지 조건
    if r == N - 1 :
        candi_list.add(su)
        return 
    
    # 이동 

    dc = [-1, 0, 1]
    for d in dc :

        nr = r
        nc = c

        nr += 1
        nc += d

        # c가 범위를 벗어나는지와 전에 움직인 방향인지 체크 
        if 0 <= nc < M and d != before_d :

            next = (nr, nc)
            dfs(next, N, M, d, candi_list, su + table[nr][nc])



N, M = map(int, input().split())

table = []

for _ in range(N) :
    line = list(map(int, input().split()))
    table.append(line)

# 그리디 아님 모두 해봐야함

candi_list = set()

# 시작지점을 0행 모두로 
for i in range(M) :
    dfs((0, i), N, M, -3, candi_list, table[0][i])


# print(candi_list)

print(min(candi_list))