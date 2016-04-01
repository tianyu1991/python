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

#Recently you invented a brand-new definition of prime numbers. For a given set of positive integers S let's call X a prime if there are no elements in S which are divisors of X (except X itself).
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
