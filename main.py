
file1 = open('text.txt', 'r', encoding='utf-8') # Открываем файл
text = file1.readlines() # Построчно считываем информацию
     
file2 = open('output.txt', 'w', encoding='utf-8') # Открываем второй файл
for line in text: # Цикл
    file2.write(line[::-1] + '\n') # Выводим строки в обратном порядке

file1.close()
file2.close()
