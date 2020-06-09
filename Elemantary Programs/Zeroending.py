mylist = []

inp1 = int(input("Enter the number of scores to be added into the list:"))

for i in range(inp1):
    inp2 = int(input("Enter the score:"))
    mylist.append(inp2)

def zeroending(mylist):

    for i in mylist:

        dat = str(i)
        
        if dat[-1] == "0":
            print(i)

        else:
            pass

zeroending(mylist)
