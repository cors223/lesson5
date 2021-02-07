with open("file_3.txt", "r") as file:
    sal = []
    poor = []
    list = file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f"Оклад меньше 20.000: {poor}. Средний оклад: {sum(map(int, sal)) / len(sal)}")