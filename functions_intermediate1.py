def randInt(min=0, max=100):
    import random
    max +=1
    max -=min
    return int(max*random.random()+min)
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))