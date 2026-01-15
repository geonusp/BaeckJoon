import sys

def input():
    return sys.stdin.readline().rstrip()

express = input()   # 50자 이하 

length = len(express)

res = 0
temp = []
flag = 1 # 1이면 + -1 이면 -
number_list = []

for i in range(0,length) :

    if express[i] == '+' :

        if len(temp) >0 and flag == 1 :
            number_list.append(int("".join(temp)))
        
        elif len(temp) > 0 and flag == -1 :
            number_list.append(-int("".join(temp)))
        
        temp = []

    elif express[i] == '-' :
        
        if len(temp) >0 and flag == 1 :
            number_list.append(int("".join(temp)))
        
        elif len(temp) > 0 and flag == -1 :
            number_list.append(-int("".join(temp)))

        temp = []
 
        flag = -1
        
    
    else :
        temp.append(express[i])

        if i == length-1 and flag == 1 :
            number_list.append(int("".join(temp)))
        elif i == length-1 and flag == -1 :
            number_list.append(-int("".join(temp)))
        
for number in number_list :
    res += number 
    
print(res)
