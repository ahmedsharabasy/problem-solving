lst = [ ]
n = int(input()) 
counter=0

for i in range(0, n): 
    element = input() 
    lst.append(element)

for i in range(0,len(lst)-1):
    if lst[i] == lst[i+1]:
        counter+=0
    elif lst[i] != lst[i+1]:
        counter +=1
print(counter+1)        



