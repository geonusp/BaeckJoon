import sys 

def input():
    return sys.stdin.readline().rstrip()

L = -1
P = -1
V = -1


i = 0

while True :
    res = 0
    i += 1

    L, P, V = map(int, input().split())

    if L != 0 and P != 0 and V != 0 :
        
        if V % P > L :
            res += L * (V//P + 1)

        else :
            res += L*(V//P) + (V%P)

        print(f"Case {i}: {res}")
    
    else : 
        break