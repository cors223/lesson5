translater = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
file = []
with open("file_4.txt", "r") as file_obj:
    for n in file_obj:
        n = n.split(" ", 1)
        file.append(translater[n[0]] + '  ' + n[1])
    print(file)

with open("file_4+.txt", "w") as file_obj_2:
    file_obj_2.writelines(file)