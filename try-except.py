def div42by(divideBy):
    
        try:
            return 42/divideBy
        except ZeroDivisionError:
            print ("Cannot divide by zero")
            


print(div42by(2))
print(div42by(6))
print(div42by(7))
print(div42by(0))
