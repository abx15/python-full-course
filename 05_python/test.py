# t = (10, 20, 30)

# print(type(t))
# print(t.index(20))
# print(t.count(10))
# print(t[-1])
# print(t[0])


students = {
    "st1": {
        "name": "Arun",
        "age": 21,
        "courseName": ["Python", "JavaScript", "PHP", "MERN"],
    },
    "st2": {
        "name": "Rohit",
        "age": 22,
        "courseName": ["Java", "C++", "MySQL"],
    },
    "st3": {
        "name": "Priya",
        "age": 20,
        "courseName": ["HTML", "CSS", "JavaScript", "React"],
    },
    "st4": {
        "name": "Neha",
        "age": 23,
        "courseName": ["Python", "Django", "Data Science"],
    },
    "st5": {
        "name": "Aman",
        "age": 24,
        "courseName": ["PHP", "Laravel", "MySQL", "JavaScript"],
    },
}

# print(students["st3"]["courseName"])

# for v in students.values():
#     print(v["name"], ":", v["courseName"])

for key,value in students.items():
    print(key, ":", value["name"], ":", value["courseName"])