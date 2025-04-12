from PyPDF2 import PdfReader,PdfWriter,errors
from pathlib import  Path

def encrypt():
    file_path = input("[+] Enter file path: ")
    file = Path(file_path)

    if not file.exists():
        print('[!] File not exist in given path. Try again')
        return

    password = input("[+] Enter encryption password: ")
    while len(password)==0:
        password = input("[+] Enter encryption password: ")
    new_file_name = input("[+] Enter new file name: ")

    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page in range(len(reader.pages)):
        writer.add_page(reader.pages[page])

    writer.encrypt(password)

    print(f"[*] Writing to {new_file_name}...")
    with open(new_file_name,'wb') as file:
        writer.write(file)
        print(f"[+] Created {new_file_name}")

def decrypt():
    file_path = input("[+] Enter file path: ")
    file = Path(file_path)

    if not file.exists():
        print("[!] File not exists in given path. Try again")
        return

    password = input("[+] Enter password for decryption: ")
    new_file_name = input("[+] Enter new file name: ")

    reader = PdfReader(file_path)
    writer = PdfWriter()

    try:
        result = reader.decrypt(password)
        if result == 0:
            print("[!] Incorrect password.")
            return
    except errors.FileNotDecryptedError:
        print("[!] Error decrypting the file.")
        return

    for page in range(len(reader.pages)):
        writer.add_page(reader.pages[page])

    print(f"[*] Writing to {new_file_name}...")
    with open(new_file_name,'wb') as file:
        writer.write(file)
        print(f"[+] Created {new_file_name}")


def main():
    choose = input("[INFO] Enter 0 to encrypt 1 to decrypt file: ").strip()
    match choose:
        case "1":
            decrypt()
        case "0":
            encrypt()
        case "quit":
            return
        case _:
            print("[!] Enter correct key")

if __name__ == "__main__":
    main()
