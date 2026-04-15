import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(start, target) :

    stack = [start]
    visited = set()


    while stack :

        current = stack.pop()
        
        # 타겟이면 
        if current == target :
            return "YES"

        # 만약 target 보다 current가 작다면
        if current < target :
            continue

        # 방문했으면 
        if current in visited :
            continue 

        visited.add(current)

        # 방문 안했으면 
        if current % 2 == 0 :
            temp1 = current // 2 
            stack.append(temp1)
        else :
            temp2 = current // 2
            temp3 = temp2 + 1
            stack.append(temp2)
            stack.append(temp3)

    return "NO"

N, M = map(int, input().split())

ans = dfs(N, M)

print(ans)