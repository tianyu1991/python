a,b=[int(n) for n in raw_input().split(" ")]
c=raw_input()
su=0
a=a%b
p=1
for g in c:
    print g
    p=(p*a)%b
    print p
    if g=="1":
        su+=p
        print su%b
    print  "su:"
    print su
print su%b


num=int(raw_input())


##Harold always boasted about his prowess with numbers. 
##So one day Reese challenged him to a problem. He gave Harold 
##two numbers X and Y and asked him to find out the Nth number
##of the series which began with X numbers of Y’s and the following
##elements are equal to the sum of the last X numbers in the series. Help Harold find the Nth number of the series
for g in range(0,num):
    x,y,n=[int(n) for n in raw_input().split(" ")]
    L=[]
    for i in range(0,x):
        L.append(y)
    for i in range(x,n):
        lnext=L[i-1]+L[i-2]+L[i-3]
        L.append(lnext)
    print L[n-1]
