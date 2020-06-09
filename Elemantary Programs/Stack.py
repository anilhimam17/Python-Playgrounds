def peek(mylist):

    if mylist == []:
        return "The List is empty"

    else:
        length = len(mylist) - 1
        return mylist[length]


def pop(mylist):

    if mylist == []:
        return "The List is empty"

    else:
        length = len(mylist) - 1

        value = mylist.pop(length)
        return value


def push(mylist, x):

    mylist.append(x)
    return peek(mylist)


def display(mylist):

    mylist.reverse()
    length = len(mylist) - 1

    for i in range(length):

        if i == 0:
            print("--->" + mylist[length])

        else:
            print(mylist[length])


#-----------------------------------------------------------------------------------------


print("Welcome to stack operations:\n\
Please enter the you list first....")

mylist = []

len_list = int(input("enter the length of the list you want to create:"))

for i in range(len_list):
    inp1 = input("Enter the elements to be added into the lists:")
    mylist.append(inp1)


while True:

    print("The Operations that can be performed on the stack are as follows:\n\
1) Push\n\
2) Pop\n\
3) Peek\n\
4) Display\n\
5) Exit")

    inp2 = input("Enter Choice :")

    if int(inp2) == 1:
        
        if len(mylist) >= len(mylist) - 1:
            print("Overflow of elements")
            

        else:
            inp3 = input("Enter push element:")
            print(push(mylist, inp3))

#-----------------------------------------------------------------------------------------

    elif int(inp2) == 2:

        if len(mylist) < 2:
            print("Underflow of elements")

        else:
            print(pop(mylist))

#-----------------------------------------------------------------------------------------

    elif int(inp2) == 3:
        print("--->" + peek(mylist))

#-----------------------------------------------------------------------------------------

    elif int(inp2) == 4:
        display(mylist)

#-----------------------------------------------------------------------------------------

    elif int(inp2) == 5:
        quit()

#-----------------------------------------------------------------------------------------

    else:
        print("The value is invalid")
        

    
