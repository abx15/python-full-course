# write a program to read a text file and count the number of words


with open("task1.txt", "r") as file:
    data = file.read().split(" ")
    print(data)
    print("word count", len(data))
