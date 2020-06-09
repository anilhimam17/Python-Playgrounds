#Factorial

class Factorial:

    def __init__(self, x):
        self.x = x

    def factorial(self):
        value = 1
        
        for i in range(1,self.x):
            value *= i

        print(value)

inp = int(input("Enter number:"))
data = Factorial(inp)
data.factorial()
            
