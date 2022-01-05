poem = """\
Программировать весело
Если работа скучна
Чтобы придать ей веселый тон -
используй Питон!!!
"""

f = open('poema.txt', 'w')
f.write(poem)
f.close()

f = open('poema.txt')

line = f.readlines()

for i in range(len(line)):
    print(line[i], end = '')

f.close()
