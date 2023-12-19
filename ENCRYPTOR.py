import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

current_directory = os.getcwd()
reports_folder = 'decrypted_reports'
files_in_folder = os.listdir(reports_folder)
output_folder = 'encrypted_reports'
output_folder_path = os.path.join(current_directory, output_folder)
os.makedirs(output_folder_path, exist_ok=True)
load_dotenv()
encrypted_key = os.getenv('KEY2')
for files in files_in_folder:
    if 'c' not in files:
        file_path = os.path.join(reports_folder, files)
        with open(file_path, 'rb') as file:
            content = file.read()
            secret_key = encrypted_key
            f = Fernet(secret_key)
            encrypt = f.encrypt(content)
            output_file_path = os.path.join(output_folder_path, files)
            with open(output_file_path, 'wb') as file:
                file.write(encrypt)