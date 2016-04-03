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

num=int(raw_input())
for g in range(0,num):
    n,t=[int(n) for n in raw_input().split(" ")]
    if t==0:
        print n
    else:
        L=[n]
        for i in range(0,t):
            n2=L[i]-L[i]/2-L[i]%2
            n2=n2-n2/4
            if L[i]==1:
                n2=0
                break
            L.append(n2)
        if n2!=0:
            print L[t]
        else:
            print 0


num=int(raw_input())
for g in range(0,num):
    nu,d=[int(n) for n in raw_input().split(" ")]
    list=[int(n) for n in raw_input().split(" ")]
    ab="Yes"
    for i in range(0,nu-1):
        if abs(list[i]-list[i+1])>d:
            ab="No"
    print ab

###Given a string, replace all the consecutively occurring characters by a single, same character.
num=int(raw_input())
for g in range(0,num):
    st= raw_input()
    st2="0"
    for i in range(0,len(st)):
        if st2[-1]!=st[i]:
            st2=st2+st[i]
    print st2[1:]


###If there are W words, word 1 is swapped with word W, word 2 is swapped with word W-1 and so on. 
num=int(raw_input())
for g in range(0,num):
    st= raw_input().split(" ")
    st2=[]
    for i in range(0,len(st)):
        st2.append(st[len(st)-i-1])
    print(" ".join(st2))



import re
num=raw_input()
if num=="a" or int(num)<1 or int(num)>10 :
    print "Invalid Test"
else:
    for g in range(0,int(num)):
        st= raw_input()
        if re.search( "([A-Za-z])",st)==None or len(st)>100:
            print "Invalid Input"
        else:
            P=re.compile("[A-Z]")
            p=re.compile("[a-z]")
            n1=0
            n2=0
            for m in P.finditer(st):
                n1+=1
            for m in p.finditer(st):
                n2+=1

            print min(n1,n2)


##Max has a rectangular prism with dimensions A, B, and C. He writes A, B, 
##and C on piece of paper. When he is not looking, Andrew replaces these numbers 
##with X=A+B, Y=B+C, and Z=A+C. Now, Max sees three numbers X, Y, Z on the 
##piece of paper. But Max needs help computing the surface area of this rectangular prism. Help him!
num=int(raw_input())
for g in range(0,num):
    x,y,z=[int(n) for n in raw_input().split(" ")]
    b=float(x+z-y)/2
    a=x-b
    c=z-b
    sur=2*(a*b+b*c+c*a)
    print "%.2f" % sur


##You are given a string, which contains entirely of decimal digits (0-9). Each digit is made of a certain number of dashes, 
##as shown in the image below. For instance 1 is made of 2 dashes, 8 is made of 7 dashes and so on

def char2num(s):
    return {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}[s]

def str2int(s):
    return reduce(lambda x,y: x+y, map(char2num, s))

st=raw_input()
print str2int(st)
