import os
import shutil


os.mkdir("Управление_файлами")


BASE_PATH = os.getcwd()
documents_name = "Управление_файлами"
os.chdir(os.path.join(BASE_PATH, documents_name))


txt_file_one = "file1.txt"
with open("file1.txt", "w", encoding='utf8') as f:
    file_one = f.write("Тестовый документ один.")


txt_file_two = "file2.txt"
with open("file2.txt", "w", encoding="utf8") as d:
    file_two = d.write("Тестовый документ два")

print(os.getcwd())
for data in os.listdir(os.getcwd()):
    print(data)


os.remove("file1.txt")


os.mkdir("Управление_файлами_директории")


NEW_PATH = os.getcwd()
new_document = "Управление_файлами_директории"
os.chdir(os.path.join(NEW_PATH, new_document))


os.chdir(os.path.join(BASE_PATH, NEW_PATH))


shutil.move(os.path.join(os.getcwd(), txt_file_two), os.path.join(NEW_PATH, new_document))


os.chdir(BASE_PATH)


shutil.rmtree("Управление_файлами")