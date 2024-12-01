number=int(input("Enter a Number: "))
count=0
if number==0 or number==1:
    print(f'{number} is neither Prime nor Composite.')
    exit()
for i in range(1,number-1):
    if number%i==0:
        count+=1

if count<2:
    print(f'{number} is Prime Number.')
else:
    print(f'{number} is Composite Number.')