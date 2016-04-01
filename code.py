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
