list1 = [20,40,55,33,34,54,90,57,65]
list2 = [10,30,55,73,34,54,60,97,45]
finelList=[]

for a in list1:
    if a in list2:
        finelList.append(a)

print(finelList)        