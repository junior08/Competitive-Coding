l=[]
c=True
while c==True:
    n=int(input())#accept input
    if n==42:
        c=False
    elif n<=99:
        l.append(n)#for the given condition 
for i in l:
    print(i)#print answer 
