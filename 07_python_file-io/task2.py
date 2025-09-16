# create a program to copy the content of one file into another

with open("task1.txt", "r") as file:
    data = file.read()
    file2 = open("copy.txt", "w")
    file2.write(data)
    file2.close()
    file.close()
