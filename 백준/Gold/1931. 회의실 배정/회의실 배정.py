import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

table = []

for _ in range(N) :

    item = list(map(int,input().split()))
    table.append(item)

sorted_table = sorted(table, key = lambda x: (x[1],x[0]))


temp = sorted_table[0][1]

count = 1

for i in range(0,N-1) : 

    if sorted_table[i+1][0] >= temp :

        temp = sorted_table[i+1][1]
        count += 1


print(count)