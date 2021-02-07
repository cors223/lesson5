def summary():
    try:
        with open("file_5.txt", "w+") as file_obj:
            line = input(f"Введите числа через пробел: ")
            file_obj.writelines(line)
            numb = line.split()

            print(sum(map(int, numb)))
    except IOError:
        print("Ошибка в файле")
    except ValueError:
        print("Неправильно набран номер. Ошибка ввода-вывода")
summary()