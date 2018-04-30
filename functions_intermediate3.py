def returnACSdictionary(min=40,max=200):
    diction = {}
    max+=1
    for i in range(min,max):
        diction[i]= chr(i)
    return diction
print(returnACSdictionary(min=65,max=90))

def upCase(str):
    newStr= ''
    for i in str:
        if ord(i) > 96:
            newStr+=(chr(ord(i)-32))
        else:
            newStr+=i
    return newStr

print(upCase('HYello'))

def lowCase(str):
    newStr= ''
    for i in str:
        if ord(i) < 91:
            newStr+=(chr(ord(i)+32))
        else:
            newStr+=i
    return newStr

print(lowCase('HYelloZ'))