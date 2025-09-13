#  count word frequency sentence = "python is fun and python is powerful"

sentence = "python is fun and python is powerful"

list = sentence.split(" ")
wordCount={}
for word in list:
    wordCount[word] = wordCount.get(word,0)+1

print(wordCount)    