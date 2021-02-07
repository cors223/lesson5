file = "file_6.txt"
subj = {}
try:
    with open(file, encoding='utf-8') as fh:
        lines = fh.readlines()

    for line in lines:
        data = line.replace('(', ' ').split()

        subj[data[0][:-1]] = sum(
            int(i) for i in data if i.isdigit()
        )
except IOError as e:
    print(e)
except ValueError:
    print(f"Не верный номер")

print(subj)