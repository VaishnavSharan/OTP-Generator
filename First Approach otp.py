n=input()
s=""
if(len(s)>=4):
    for i in range(1,len(n),2):
        s+=str((int(n[i])**2))
    print(s[:4])
else:
    print("-1")