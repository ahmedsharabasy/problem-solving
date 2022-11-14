#1200


#2 4 7 8 10
n=input()

for i in n:
    paridad=0
    a =  list(map(int, input().split( )))
    if (a[i]%2 == 0):
        paridad+=1
    if paridad > 1:
        for i in range(n):
            if (a[i]%2 != 0):
                index = i 
    else:
        for i in range(n):
            if (a[i]%2 == 0):
                index = i  


