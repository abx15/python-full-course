# create a file and store 5 line using writelines()

file = open("task4.txt", "w")
file.writelines(
    "This is line 1\n",
    "This is line 2\n",
    "This is line 3\n",
    "This is line 4\n",
    "This is line 5\n",
)

file.close()