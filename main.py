from cryptography.fernet import Fernet
secret_key = Fernet.generate_key()
print(secret_key)
fernet_key = Fernet(secret_key)
data = b'Hello World'
encrypted_data = fernet_key.encrypt(data)
decrypted_data = fernet_key.decrypt(encrypted_data)
print(encrypted_data)
print(decrypted_data)
# print(key)