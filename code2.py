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
num=int(raw_input())
for g in range(0,num):
    x,y,n=[int(n) for n in raw_input().split(" ")]
    if x>=n:
        print y
    else:
        if y==0:
            print 0
        else:
            L=[]
            for i in range(0,x):
                L.append(y)
            for i in range(x,n):
                lnext=sum(L)
                L.append(lnext)
                L.pop(0)
            print L[x-1]
