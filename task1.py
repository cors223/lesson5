file = open("file_1.txt", "w")
line = input(f"Введите текст: ")
while line:
    file.writelines(line)
    line = input(f"Введите текст: ")
    if not line:
        break

file.close()
file = open("file_1.txt", "r")
content = file.readlines()
print(content)
file.close()
