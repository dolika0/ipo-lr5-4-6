with open('text.txt', 'r', encoding='utf-8') as infile:#чтение информации из файла text.txt
    spis = infile.readlines()#инициализация переменной spis

with open('output.txt', 'w', encoding='utf-8') as outfile:#запись информации в файл output.txt
    for line in spis:#цикл for
        outfile.write(line[::-1] + '\n')#запись строки в обратном порядке
