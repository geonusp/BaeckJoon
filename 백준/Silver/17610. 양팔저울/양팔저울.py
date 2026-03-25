import sys

def dfs(idx, current_weight, chus, candi) :
    # 끝에 도달하면 
    if idx == len(chus) :
        if current_weight > 0 :
            candi.add(current_weight)
        return 
    


    # +
    dfs(idx+1, current_weight + chus[idx], chus, candi)
    # -
    dfs(idx+1, current_weight - chus[idx], chus, candi)
    # 0
    dfs(idx+1, current_weight, chus, candi)

def input():
    return sys.stdin.readline().rstrip()


k = int(input())

chus = list(map(int, input().split()))

candi = set()

dfs(0, 0, chus, candi)

res = sum(chus) - len(candi)

print(res)







