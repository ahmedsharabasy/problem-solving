x=input()
upper=0
lower=0

for i in x:
    if i.islower():
        lower+=1
    else:
        upper+=1

if lower > upper:
    print(x.lower())
elif lower < upper:
    print(x.upper())
else:
    print(x.lower())                
