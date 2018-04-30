def countDown(num):
    numList = []
    for i in range(num, -1, -1):
        numList.append(i)
    return numList
print(countDown(5))

def returnTwo(arr):
    print(arr[0])
    return arr[1]
print(returnTwo([2,4]))

def returnSum(arr):
    sum = arr[0]+len(arr)
    return sum
print(returnSum([5,2,3,4,5]))

def returnsSecond(arr):
    newList = []
    count = 0
    for i in range(0,len(arr)):
        if arr[i]>arr[1]:
            newList.append(arr[i])
            count+= 1
    if newList:
        print(count)
        return newList
    else:
        return False
print(returnsSecond([33,6,57,523,4]))

def thisThat(num1,num2):
    newList=[]
    for i in range(0,num1):
        newList.append(num2)
    return newList
print(thisThat(4,3))
