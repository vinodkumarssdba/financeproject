num=456
total=0
while(num>0):
    i=num%10
    total+=i
    num//=10
print(total)