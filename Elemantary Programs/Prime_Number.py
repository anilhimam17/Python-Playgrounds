inp = int(input("Enter number to check whether it is a prime:"))

def Prime_Number(inp, i = 2):

    if inp <= 2:
        return True if inp == 2 else False   #For 2 as a prime number

    elif inp % 2 == 0:                       #Divisible by 2 is not a prime
        return False

    elif i * i > inp:                        #To check divisibility
        return True

    return Prime_Number(inp, i + 1)

print(Prime_Number(inp))
