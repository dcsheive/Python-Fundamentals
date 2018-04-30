for count in range(0,151):
    print(count)
for count in range(5,1000000):
    if count%5==0:
        print(count)

for count in range(1,101):
    if count%5==0 and count%10!=0:
        print('Coding')
    elif count%10==0:
        print('Dojo')
    else:
        print(count)
sum=0
for count in range(0,500000):
    if count%2==1:
        sum+=count
print(sum)
count =2018
while count>0:
    print(count)
    count=count-4
lowNum= 2
highNum = 9
mult = 3
for count in range(highNum,lowNum,-1):
    if count%mult==0:
        print(count)
