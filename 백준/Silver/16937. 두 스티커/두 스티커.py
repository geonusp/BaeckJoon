import sys 
from itertools import combinations

def is_full_and_res(a, b, s_list, s) :
    if 0 < a <= H and 0 < b <= W :
        s_list.append(s)

def input():
    return sys.stdin.readline().rstrip()

H, W = map(int, input().split())

N = int(input())

stickers = []

for _ in range(N) :
    line = tuple(map(int, input().split()))
    stickers.append(line)


two = list(combinations(stickers, 2))

s_list = [0]

for pair in two :

    sticker1 = pair[0]
    sticker2 = pair[1]

    shape1 = [(sticker1[0], sticker1[1]), (sticker1[1], sticker1[0])]
    shape2 = [(sticker2[0], sticker2[1]), (sticker2[1], sticker2[0])]

    s = (sticker1[0] * sticker1[1]) + (sticker2[0] * sticker2[1])

    # 총 4번 
    for r1, c1 in shape1 :
        for r2, c2 in shape2 :
            
            is_full_and_res(max(r1, r2), c1+c2, s_list, s)
            is_full_and_res(r1 + r2, max(c1, c2), s_list, s)

print(max(s_list))