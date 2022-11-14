n,h=map(int, input().split())
th=map(int,input().split())
width_of_road=0
for i in th:
    if i > h: width_of_road+=2
    else: width_of_road+=1

print(width_of_road)    



n, h = map(int, input().split())
a =  list(map(int, input().split()))
t = 0
for i in a:
	if i > h: t += 2
	else: t += 1
print (t)

