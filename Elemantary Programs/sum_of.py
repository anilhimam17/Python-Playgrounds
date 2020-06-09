mylist = [1,2,3,4,5,6,7,8,9]
length = len(mylist) - 1

def list_sum(mylist):

    if mylist == []:  #If list is empty
        return 0

    else:
        return mylist[0] + list_sum(mylist[1:])  #Starts with the Zeroth Element
        
print(list_sum(mylist))
