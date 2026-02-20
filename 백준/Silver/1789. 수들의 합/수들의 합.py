import sys

def input():
    return sys.stdin.readline().rstrip()

S = int(input())

start = 1
end = S
res = 0

while start <= end :
    
    mid = (start+end) // 2

    sum_mid = (mid*(mid+1)) // 2

    if sum_mid < S :
        res = mid
        start = mid + 1
        

    elif sum_mid == S :
        res = mid 
        break

    elif sum_mid > S :
        end = mid - 1


print(res)

