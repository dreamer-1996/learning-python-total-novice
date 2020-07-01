def printName(name):
    print ("Hi my name is " + name)
    return len(name)
myName = ''
print ("Please provide your name as input")
myName = input()
print("Length of my name is " + str(printName(myName)))
