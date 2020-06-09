''' To read a file line by line...
    To remove the lines from the file that start with a...'''


myfile1 = open('myfile1.txt', 'r')
lines = myfile1.readlines()
    

myfile2 = open('myfile2.txt', 'a')
for i in lines:

    if i[0] == "A":
        myfile2.write(i)

    else:
        pass



