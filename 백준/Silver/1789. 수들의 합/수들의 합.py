import sys

def input():
    return sys.stdin.readline().rstrip()

S = int(input())

sum = 0

sum_list = set()

i = 0

while True :

    i += 1
    temp = sum + i
    if temp > S :
        sum_list.add(i)
        sum_list.remove(temp-S)
        break
        

    elif temp == S :
        sum_list.add(i)
        sum = temp
        break

    elif temp < S :
        sum_list.add(i)
        sum = temp

print(len(sum_list))