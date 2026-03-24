import sys
from itertools import combinations 

def input():
    return sys.stdin.readline().rstrip()


def is_full_and_res(a, b,s) :
     
    if 0 < a <= H and 0 < b <= W : 
            ans_list.append(s)
     

H, W = map(int, input().split())

N = int(input())

candi = []

for _ in range(N) :
    line = tuple(map(int, input().split()))
    candi.append(line)

can = list(combinations(candi, 2))

# 탐색 -> 스티커들 크기되는지 + 범위 안넘는지 -> 스티커 넣기 mCn

ans_list = [0] # 안전 장치(스티커 하나도 못넣을때를 대비)

for item in can :

    s = (item[0][0] * item[0][1]) + (item[1][0] * item[1][1])

    # 1번 스티커가 가질 수 있는 모양 (원본, 회전)
    shape1 = [(item[0][0], item[0][1]), (item[0][1], item[0][0])]
    # 2번 스티커가 가질 수 있는 모양 (원본, 회전)
    shape2 = [(item[1][0], item[1][1]), (item[1][1], item[1][0])]

    for r1, c1 in shape1 :
        for r2, c2 in shape2 :
            # 세로로 나란히 
            is_full_and_res(max(r1,r2), c1 + c2, s)
            # 가로로 나란히 
            is_full_and_res(r1 + r2, max(c1, c2), s)

print(max(ans_list))