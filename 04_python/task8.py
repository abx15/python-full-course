l = [10, 30, 20, 30, 10, 40, 50, 20, 60, 30, 90, 80]


unElement=[]

for a in l:
    if a not in unElement:
        unElement.append(a)
# print(unElement)   

print(sorted(list(set(l))))     