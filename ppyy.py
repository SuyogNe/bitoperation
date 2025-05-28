def powerof8(number):
    bitposition=0
    mask=1

    while (bitposition <=63):
        mask<<=bitposition

        if (mask == number):
            return True
        
        bitposition+=3
        mask=1
        return False
    
number = int(input("Enter a number: "))
if (powerof8(number)):
    print("The number is a power of 8")
else:
    print("The number is not a power of 8")