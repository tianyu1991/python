def reverse(str):
    if isinstance(str,int)==1:
        return ""
    else:
        str2=""
        for i in str:
            str2=i+str2
        return str2
    
def case(li):
    for i in li:
        print reverse(i)
    return ""
    

#ana
def fun(str1,str2):
    if len(str1)!=len(str2):
        return 0
    else:
        for i in str1:
            if i not in str2:
                return 0
            else:
                if str1.count(i)!=str2.count(i):
                    return 0
        return 1
                
print fun("ABSS","BSAS")   
print fun("ABSCS","ABCSC")

#Given a number find the number of trailing zeroes in its factorial.
N=int(raw_input())
sum=1
for n in range(1,N+1):
    sum=sum*n

N2=0
while sum%10==0:
    sum=sum//10
    N2+=1
print N2

#Recently you invented a brand-new definition of prime numbers.
#For a given set of positive integers S let's call X a prime if there are no elements in S which are divisors of X (except X itself).
def fun(li):
    li2=[]
    for i in li:
        p=0
        for n in li:
            if (i%n==0) and (i!=n):
                p=1
        if p==0:
            li2.append(str(i))
    return li2

n=raw_input()
li=[int(n, 10) for n in raw_input().split(" ")]

if n==0:
    li2=li
else:
    li2=fun(li)

print(" ".join(li2))

#Panda has started learning about subsets.
#His professor gave him a simple task. Given a list of numbers, Panda has to choose the subset which gives the maximum product. 
#However, the professor asked Panda only to submit the maximum product obtained by taking exactly two numbers from the list. Please help Panda in finding out the answer to this assignment.

num=int(raw_input())
mylist=[int(n, 10) for n in raw_input().split(" ")]

def fun(li):
    m1=0
    m2=0
    l1=0
    l2=0
    for i in li:
        if i>m1 :
            m2=m1
            m1=i
        else:
            if i>m2:
                m2=i
        if i<l1:
            l2=l1
            l1=i
        else:
            if i<l2:
                l2=i
    if (m1*m2)>(l1*l2):
        return m1*m2
    else:
        return l1*l2

if num==2:
    print mylist[0]*mylist[1]
else:
    print fun(mylist)
import math
num=int(raw_input())
for i in range(0,num):
    mylist=[int(n, 10) for n in raw_input().split(" ")]
    a=mylist[0]
    H=mylist[1]
    angle=mylist[2]
    h=H-abs(a*math.tan(angle*3.141593/180)/2//1)
    if h>=1:
        print int(h)
    else:
        h2=H/math.tan(angle*3.141593/180)*H/a/2
        print h2
        
        if h2 % 1==0:
            print int(h2)
        else:
            print int(h2//1+1)
###78 57 82 9

import math
num=int(raw_input())
for i in range(0,num):
    mylist=[int(n, 10) for n in raw_input().split(" ")]
    a=mylist[0]
    H=mylist[1]
    angle=mylist[2]
    h=H-abs(a*math.tan(angle*3.141593/180)/2//1)
    if h>H/2.0:
        print int(h)
    else:
        h2=H/math.tan(angle*3.141593/180)*H/a/2
        if h2 % 1==0:
            print int(h2)
        else:
            print int(h2//1+1)

##Big P is fairly good in mathematics.
##His teacher has asked him to add two numbers.
##Now , Big P has a problem that he sometimes writes a '6' as a '5' and vice versa.
##Given two numbers, A and B, calculate the minimum and the maximum sum Big P could possibly get.

Input:
mylist=[n for n in raw_input().split(" ")]
ma=0
mi=0
for n in mylist:
    if n.find("5")+n.find("6")==-2:
        ma+=int(n)
        mi+=int(n)
    else:
        if (n.find("5")!=-1) and (n.find("6")!=-1):
            if int(n)>0:
                ma+=int(n.replace("5","6"))
                mi+=int(n.replace("6","5"))
            else:
                ma+=int(n.replace("6","5"))
                mi+=int(n.replace("5","6"))
        else:
            if n.find("5")!=-1:
                if int(n)>0:
                    ma+=int(n.replace("5","6"))
                    mi+=int(n)
                else:
                    ma+=int(n)
                    mi+=int(n.replace("5","6"))
            if n.find("6")!=-1:
                if int(n)>0:
                    mi+=int(n.replace("6","5"))
                    ma+=int(n)
                else:
                    mi+=int(n)
                    ma+=int(n.replace("6","5")) 
print str(mi)+" "+str(ma)
