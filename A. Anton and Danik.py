from itertools import count


n=int(input())
s=list(input())

for i in range(n):
    if s.count("A")==s.count("D"):
        print("Friendship")
        break
    elif s.count("A") > s.count("D"):
        print("Anton")
        break
    else: 
        print("Danik")
        break



    