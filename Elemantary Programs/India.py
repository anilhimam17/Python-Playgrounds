myfile = open("INDIA.txt", "r")
lines = myfile.readlines()

len_lines = len(lines)

count = 0

for i in range(len_lines):
    
    if "India" in len_lines[i]:
        count += 1
        print("The line number is:", i)
        print(mylist[i])

    else:
        pass


print("The occurences of india in the given file is:", count)
