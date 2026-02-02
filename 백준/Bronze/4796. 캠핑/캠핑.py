import sys 

def input():
    return sys.stdin.readline().rstrip()

L = 100
P = 100
V = 100


i = 1

while True :

    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0 :
        break

    count = V // P

    if V - (P * count) > L :
        res = (count+1) * (L)
    else :
        res = V - (count * (P-L))

    print(f"Case {i}: {res}")

    i += 1

    if L == 0 and P == 0 and V == 0 :
        break
    
