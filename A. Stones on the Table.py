x=int(input())
a=[x for x in input().replace('',' ').split()]
count=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count+=1

print(count)