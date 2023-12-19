import os
reports_folder = 'decrypted_reports'
# os.listdir возвращает список имен файлов и директорий в заданной директории.
files_in_folder = os.listdir(reports_folder)
#это будем добавлять в конце строки
check = "Проверено!"
# Открываем каждый файл
for files in files_in_folder:
    #Указываем путь файла
    file_path = os.path.join(reports_folder, files)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()
        updated_content = content.replace('вра', 'дру')
        updated_content = updated_content + check
        print(updated_content)
    # Перезаписываем контент
    with open(file_path, 'w', encoding='utf-8') as file:
        content1 = file.write(updated_content)
