import sys

def input():
    return sys.stdin.readline().rstrip()

S = int(input())

num = 0

num_list = set()

num_sum = 0

while True :

    num += 1

    num_sum += num

    num_list.add(num)

    if S == num_sum :
        break

    elif S < num_sum :
        num_list.remove(num_sum-S)
        break

    elif S > num_sum :
        continue

print(len(num_list))

