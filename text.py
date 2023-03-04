# открываем файл
with open('filename.txt', 'r') as f:
    # читаем содержимое файла
    lines = f.readlines()

# выводим содержимое файла построчно
for line in lines:
    print(line.strip())
