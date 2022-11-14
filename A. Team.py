num_problems=int(input())
sum=0
for n in range(num_problems):

    x,y,z=map(int,input().split())

    if x+y+z >=2:
        sum+=1



print(sum)        
