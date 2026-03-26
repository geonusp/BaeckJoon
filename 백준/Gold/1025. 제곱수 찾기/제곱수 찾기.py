import sys
import math

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

table = []

candi_list = [-1] # 비어있는 것 예외 처리 

for _ in range(N) :
    line = list(map(int, input()))
    table.append(line)

for i in range(N) :
    for j in range(M) :
        # 시작점
        # 어떤 보폭으로 뛸지 (행, 열)
        for k in range(-N,N) :
            for l in range(-M, M) :
                if k == 0 and l == 0 : # 제자리에 있는거 방지 
                    continue

                r, c = i, j
                num_str = ""
                
                while 0 <= r < N and 0 <= c < M :
                    num_str += str(table[r][c])
                
                    r += k
                    c += l
                
                    num = int(num_str)
                    # 만약 num_str이 제곱수면
                    sqrt_n = math.isqrt(num) # 부동소수점 오차방지 
                    if sqrt_n **2 == num : 
                        candi_list.append(num)

print(max(candi_list))
                        



