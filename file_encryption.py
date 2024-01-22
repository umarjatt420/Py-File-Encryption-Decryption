from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(file_path):
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_path):
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
    cipher = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path[:-10], "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

def main():
    generate_key()
    choice = input("1 => Encrypt a File\n2 => Decrypt a File\nSelect Option: ")
    if choice == '1':
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path)
        print("File encrypted successfully.")
    elif choice == '2':
        file_path = input("Enter the path of the file to decrypt: ")
        decrypt_file(file_path)
        print("File decrypted successfully.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()