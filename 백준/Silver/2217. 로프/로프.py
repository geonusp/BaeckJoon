import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

rope_list = []

candidate = []

res = 0 

for _ in range(N) :
    rope_list.append(int(input()))

sorted_rope_list = sorted(rope_list, reverse = True)

for i in range(0, N) :
    candidate.append(sorted_rope_list[i])

    temp = candidate[i] * len(candidate) 
    if temp > res :
        res = temp

print(res)
