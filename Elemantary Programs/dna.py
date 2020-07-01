def main():

    #DNA Sequence Input
    dna_seq = input("Please enter the dna sequence: ")
    length = len(dna_seq)

    #Strs based for the calculation
    strs = {"AGAT": 0, "AATG": 0, "GATA": 0, "TATC": 0, "GAAA": 0, "TCTG": 0, "TCTAG": 0, "AGATC": 0, "TTTTTTCT": 0}

    #Index for the while loop
    index = 0

    #Repeater
    rep = ""

    #Counter
    count = 0

    while (index < length):

        #Checking for the presence of the given str in the substring
        if rep == "":
            pass
        
        else:
            if dna_seq[index: index + len(rep)] != rep:
                count = 0

        if dna_seq[index: index+4] in ["AGAT", "AATG", "GATA", "TATC", "GAAA", "TCTG"]:

            count += 1
            rep = dna_seq[index: index+4]
            strs[rep] = count
            index += 4

        elif dna_seq[index: index+5] in ["TCTAG", "AGATC"]:

            count += 1
            rep = dna_seq[index: index+5]
            strs[rep] = count
            index += 5

        elif dna_seq[index: index+8] == "TTTTTTCT":

            count += 1
            rep = dna_seq[index: index+8]
            strs[rep] = count
            index += 8

        else:
            index += 1

    print("The counts for all the strs are: \n", strs)


main()
