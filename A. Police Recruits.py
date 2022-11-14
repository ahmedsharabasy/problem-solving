x=int(input())
a=[int(x) for x in input().split()]
crimes_count=0
manpower_count=0

for i in range(x):   
    if a[i] >= 1:        
        manpower_count+=a[i]
    if a[i] == -1:
        manpower_count -=1 
    if manpower_count < 0 :      
        crimes_count+=1
        manpower_count = 0  
print(crimes_count)