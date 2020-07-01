def main():

    dna_seq = input("Enter the DNA Sequence: ")
    length = len(dna_seq)

    strs = {"AGATC": [], "TTTTTTCT": [], "AATG": [], "TCTAG": [], "GATA": [], "TATC": [], "GAAA": [], "TCTG": []}
    i = 0
    rep = ""
    count = 0

    while i < length:

        if dna_seq[i: i + len(rep)] != rep and rep != "":
            strs[rep].append(count)
            count = 0
            rep = ""

        if dna_seq[i: i+8] == "TTTTTTCT":
            count += 1
            rep = "TTTTTTCT"
            i += 8

        elif dna_seq[i: i+5] in ["AGATC", "TCTAG"]:
            count += 1
            rep = dna_seq[i: i+5]
            i += 5

        elif dna_seq[i: i+4] in ["AATG", "GATA", "TATC", "GAAA", "TCTG"]:
            count += 1
            rep = dna_seq[i: i+4]
            i += 4

        else:
            i += 1

    for i, j in strs.items():
        print(i, max(j))


main()

        
