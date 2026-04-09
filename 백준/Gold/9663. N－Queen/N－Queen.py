import sys

from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()

def is_wrap(r,c) :
    
    for i in range(r) :

        # 같은세로줄 또는 같은 대각선에 있다면  
        if row_board[i] == c or abs(row_board[i]-c) == abs(i-r) :
            return True
        
    return False
        

def dfs(r):

    global count

    # 종료 조건 
    if r == N :
        count += 1
        return 
    
    for c in range(N) :
        # 겹치지 않는가  
        if not is_wrap(r,c) :
            # 퀸 놓음 
            row_board[r] = c
            
            # 다음 행으로 
            dfs(r+1)
            # 백트래킹 
            

N = int(input())

row_board = [0] * N

# 모두 넣어서 콤비네이션 돌릴 시 최대 64C14 = 약 47조 -> 메모리초과, 시간초과 
# 줄여야만함!

# 일단 퀸 규칙 일부 중 하나가 같은 행에는 퀸이 놓이면 안된다는걸 적용 -> 14! = 약 870억....
# 조합과 순열은 무지성으로 넣기때문에 가지치기가 안됨 -> dfs(백트래킹포함) 이용해 직접 구현 
#  

count = 0

dfs(0)

print(count)
