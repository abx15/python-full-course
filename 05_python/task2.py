# swap keys and values data = {'a':1,'b':2,'c':3}
data = {"a": 1, "b": 2, "c": 3}
finelAns = {}

for k, v in data.items():
    finelAns[v] = k
print(finelAns)
