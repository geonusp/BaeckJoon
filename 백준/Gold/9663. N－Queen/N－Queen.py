import sys

def input():
    return sys.stdin.readline().rstrip()

# (r, row_board[r])
def is_wrap(r,c) :

    # 겹치는지 확인 가로, 대각선  
    for i in range(r) :
        if row_board[i] == c or abs(row_board[i] - c) == abs(i - r) :
            return True
    # 안겹치면 false
    return False


def dfs(r):

    global count

    # 안 겹치고 모두 탐색했으면  
    if r == N :
        count += 1
        return 
        
    # 가로 순회 
    for c in range (N) :

        # 반경 겹치는가(뻗어서 확인)
        if not is_wrap(r,c) :
            # 마킹 
            row_board[r] = c  
            #안겹치면 쭉가기
            dfs(r+1) 
            # 어차피 아래로만 이동해서 백트래킹 필요없음  
        



N = int(input())

row_board = [0] * N

count = 0

dfs(0)

print(count)