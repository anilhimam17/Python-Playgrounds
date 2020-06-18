inp = input("Enter the card number: ")

def luns_algo(inp):

    even_val = []
    for i in range(len(inp) - 2, - 1, -2):
        even_val.append(inp[i])

    print(even_val)

luns_algo(inp)
