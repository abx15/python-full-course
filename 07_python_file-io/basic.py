# file =open("demo.txt","w")
# file.write("Welcome to python \n")
# file.write("Welcome to New World \n")
# file.writelines("kya hal hai \n" "aur batao kaise ho \n")
# file.close


with open("demo.txt", "r") as file:
    print(file.read())
