import os

file_list = []
for file in os.listdir():
    if file.find('txt') != -1:
        file_list.append(file)
merge_file_list = []
for file in file_list:
    with open(file, encoding='UTF-8') as tmp_file:
        text_file = [line.strip() for line in tmp_file]
        merge_file_list.append([file, len(text_file), text_file])
    merge_file_list.sort(key=lambda x: x[1])
    with open('./merge/merge_file.txt', 'w', encoding='UTF-8') as f:
        for merge_file in merge_file_list:
            f.write(f'{merge_file[0]}\n')
            f.write(f'{merge_file[1]}\n')
            for line in merge_file[2]:
                f.write(f'{line}\n')
