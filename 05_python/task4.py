#  find key with max values core ={'Alice':50,'Bob':70,'Charlie':65}


core = {"Alice": 50, "Bob": 70, "Charlie": 65}
maxValueKey = ""
maxValue = 0

for k, v in core.items():
    if v > maxValue:
        maxValue = v
        maxValueKey = k
print(maxValue, maxValueKey)
