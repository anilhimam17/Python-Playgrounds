def main():

    #Takes the input for the credit card number
    card_number = input("Number: ")

    #Deploys Luhn's Algorithm on the given card number
    result = luhns_algo(card_number)

    #Prints result
    print(result)


#Function for Luhn's algorithm
def luhns_algo(card_number):

    length = len(card_number)
    for i in range(length - 1, -1, -1):
        print(card_number[i])

    return 0


#The main function to run the program
if __name__ == "__main__":
    main()

luns_algo(inp)
