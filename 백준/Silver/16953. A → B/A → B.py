import sys

def input():
    return sys.stdin.readline().rstrip()

A, B = map(int, input().split())

res = 1

while True :
    if B < A :
        print(-1)
        break
    elif B == A :
        print(res)
        break

    if B % 2 == 0 :
        B = B // 2
    elif B % 2 == 1 and (B-1) % 10 == 0 :
        B = (B - 1) // 10
    elif B % 2 == 1 and (B-1) % 10 != 0 :
        print(-1)
        break

    res += 1



