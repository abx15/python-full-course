# write a function to find how many times a word appears in a file


def getMyWord(fileName, word):
    with open("task3.txt", "r") as file:
        data = file.read().lower().split()
        countMyWord = data.count(word)
        # print(countMyWord)
        return countMyWord


print(getMyWord("task3.txt", "python"))
