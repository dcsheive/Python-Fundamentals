def biggie(arr):
    for i in range(0,len(arr)):
        if arr[i]>0:
            arr[i] = 'big'
    return arr
print(biggie([-1,-3,4,-5,5]))

def countPos(arr):
    count = 0
    for i in range(0,len(arr)):
        if arr[i]>0:
            count = count+1
    arr[len(arr)-1]= count
    return arr
print(countPos([1,-2,3,-4,-5,6]))

def sumTotal(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum+=arr[i]
    return sum
print(sumTotal([1,3,4,2]))

def avg(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    sum/=len(arr)
    return sum
print(avg([1,2,3,4,4]))

def length(arr):
    return len(arr)
print(length([1,2,3,3]))

def min(arr):
    if arr:
        min = arr[0]
        for i in range(1,len(arr)):
            if arr[i]<min:
                min = arr[i]
        return min
    else:
        return False
print(min([1,2,23,0]))

def max(arr):
    if arr:
        max = arr[0]
        for i in range(1,len(arr)):
            if arr[i]>max:
                max = arr[i]
        return max
    else:
        return False
print(max([1,2,23,0]))

def ult(arr):
    max = arr[0]
    sum = arr[0]
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] <min:
            min = arr[i]
        sum += arr[i]
    avg =sum/len(arr)
    dict = {
        "sum": sum,
        "average": avg,
        "maximum": max,
        "minimum": min,
        "length": len(arr)
    }
    return dict
print(ult([2,3,3,45,5]))

def reverseList(arr):
    for i in range(0,int(len(arr)/2)):
        temp = arr[i]
        arr[i]= arr[len(arr)-1-i]
        arr[len(arr) - 1 - i]= temp
    return arr
print(reverseList([1,3,2,4,5]))
