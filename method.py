def map(list, function):
    for i in range(0,len(list)):
        list[i] = function(list[i])
    return list

def reduce(list, function):
    sum = 0
    for i in range(0,len(list)):
        sum+= function(list[i])
    return sum

def find(list, function):
    for i in range(0,len(list)):
        if function(list[i]):
            return list[i]
    return False

def filter(list, function):
    newList= []
    for i in range(0,len(list)):
        if function(list[i]):
            newList.append(list[i])
    if newList:
        return newList
    else:
        return False

def reject(list, function):
    newList = []
    for i in range(0, len(list)):
        if not function(list[i]):
            newList.append(list[i])
    if newList:
        return newList
    else:
        return False

