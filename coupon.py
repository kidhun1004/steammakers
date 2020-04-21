import random

nu = 0
trial = 0
coupon=[]

c = 5
n = 500
req = 2

def listcheck(co):
    count = 0
    for i in range(0,c):
        if co[i] >= req:
            count += 1
        
    if count == c:
        return False
    else:
        return True

for i in range(0,n):
    coupon = [0 for i in range(c)]

    while(listcheck(coupon)):
        random.seed()
        nu = random.randrange(0,c)

        print(nu)

        coupon[nu] += 1

        print(coupon)
        
    print("")
    trial += sum(coupon)

print(trial/n)

        


