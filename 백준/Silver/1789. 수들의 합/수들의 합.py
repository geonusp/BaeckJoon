import sys

def input():
    return sys.stdin.readline().rstrip()

S = int(input())

start = 1 # 자연수의 개수 
end = S
res = 0

while start <= end :
    mid = (start+end) // 2
    sum_mid = (mid*(mid+1)) // 2   # 1부터 mid 까지 합 

    if sum_mid > S :
        end = mid - 1

    elif sum_mid == S :
        res = mid 
        break

    elif sum_mid < S :
        start = mid + 1
        res = mid 
        


print(res)





