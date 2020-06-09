print("Welcome to Palindrome.py")

inp = input("Enter String to Find the Palindrome:")

def Palindrome(inp):

    if len(inp) > 0 and len(inp) < 2:
        return 0

    else:
        return Palindrome(inp[1:-1])

print(Palindrome(inp))
