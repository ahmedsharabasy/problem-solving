x=input().lower()
distinct=''.join(set(x))

if len(distinct)%2==0:
    print("CHAT WITH HER!") 
else:
    print("IGNORE HIM!")    