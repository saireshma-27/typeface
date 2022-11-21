digits=[0,1,2,5,6,8,9]

def valid(k):
    k=str(k)
    for i in k:
        if int(i) not in digits:
            return False
    return True

n = int(input())
if n < len(digits):
    print(digits[n])
else:
    count=len(digits)
    k=digits[-1]
    while(count<=n):
        k+=1
        if valid(k):
            count+=1
    print(k)
