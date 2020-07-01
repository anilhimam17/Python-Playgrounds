inp = input("Enter string:")

mydict = {"AGAT" : 0, "AATG" : 0}
count = 0
rep = ""

i = 0
while i < len(inp):

    if rep == "":
        pass
    else:
        if rep != inp[i:i+4]:
            count = 0
        else:
            pass
    
    if inp[i:i+4] in ["AGAT", "AATG"]:
        count += 1
        rep = inp[i:i+4]
        mydict[rep] = count
        i += 4

    else:
        i += 1

print(f"The total no of occurences are: {count}")
print(f"The dictionary after the program was:\n {mydict}")
