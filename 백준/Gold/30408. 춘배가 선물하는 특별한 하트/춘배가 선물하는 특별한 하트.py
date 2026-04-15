import sys

def input():
    return sys.stdin.readline().rstrip()


def dfs(start, target) :

    
    stack = [start]
    visited = set()

    # 없으면
    while stack :

        current = stack.pop()

        # 목표인지 확인 
        if current == target :
            return "YES"
        # 방문했는지 체크
        if current in visited :
            continue

        visited.add(current)
        
        if current % 2 == 0 :

            temp1 = current//2
            stack.append(temp1)
            

        else :
            temp2 = (current - 1) // 2
            temp3 = ((current-1) // 2) + 1 

            stack.append(temp2)
            stack.append(temp3)

    return "NO"


N, M = map(int, input().split())

# dfs + dp ?
ans = dfs(N,M)

print(ans)
