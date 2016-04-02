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
