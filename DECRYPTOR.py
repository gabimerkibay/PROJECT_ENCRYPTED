import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from datetime import datetime, timedelta
# Для понимания будут комменты
#Создаем даты для того чтобы по ним пройтись и искать файл
start_time = datetime(2023, 10, 1)
end_time = datetime(2023, 10, 31)
#Current_time будет менять значение начиная от старт тайм
current_time = start_time
#Чтобы ключ не украли и не дешифровали создаем папку .env и туда закинем ключь и ниже две комнды чтобы запустить и найти значение KEY
load_dotenv()
secret_key = os.getenv('KEY1')
fernet_key = Fernet(secret_key)
# Название файла и команда makedirs создает эту папку exist_ok=True нужен для того чтобы при повторном запуске файл еще раз не создавался
output_folder = 'decrypted_reports'
os.makedirs(output_folder, exist_ok=True)
prefixes = ['cachalot', 'whale', 'cheetah', 'gorilla', 'dolphin', 'tiger', 'elephant', 'giraffe', 'penguin', 'koala']
#Заходим в цикл начиная от старт до енд тайм
while current_time <= end_time:
    #Дату переводим в строку
    date_str = current_time.strftime("%d_%m_%Y")
    # Условная команда для проверки существования файла если нет False если есть True
    file_found = False
    #Заходим в цикл для присваивания префикса на дату
    for prefix in prefixes:
        #Будем записывать название файла и искать по нему в дальнейшем
        file_name = f"spy_reports/{date_str}_{prefix}.txt"
        #Создаем путь на декриптер репортс файл
        decrypted_file_path = os.path.join(output_folder, f"{date_str}_{prefix}.txt")
        #Если есть файл с таким называнием то os.path.exists вернет просто True поэтому можно не указывать условие так как команда ялвяется условием
        if os.path.exists(file_name):
            print(f"File found: {file_name}")
            # Если нашли файл открывем и читаем
            with open(file_name, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()
            #Дешифруем этот файл
            decrypted_data = fernet_key.decrypt(encrypted_data)
            #Дешифрованный файл записываем в новый файл
            with open(decrypted_file_path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)
            # Условная команда меняет значение так как мы нашли файл
            file_found = True
        else:
            continue
    # Если условная команда file_found не поменял значение то есть он остался False то пишем по такой то дате файла нет
    if not file_found:
        print(f"No file found for {date_str}")
    # В каррент тайм добавляем плюс один и зааааново все проходим пока смерть не разлучит этот цикл ну или просто наступит 31 октября
    current_time += timedelta(days=1)