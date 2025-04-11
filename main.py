from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

def encrypt():
    file_path = input("[+] Enter file path: ").strip()
    file = Path(file_path)

    if not file.exists():
        print("[!] File not found. Try again")
        return

    encrypt_password = input("[+] Enter password for encrypt: ")
    new_file_name = input("[+] Enter new encrypted file name: ")

    writer = PdfWriter()
    try:
        reader = PdfReader(file_path)

        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

        writer.encrypt(encrypt_password)
        with open(new_file_name, 'wb') as file:
            writer.write(file)

        print(f"[+] Created {new_file_name}")
    except Exception as e:
        print(f"[!] Error: {e}")


def decrypt():
    file_path = input("[+] Enter file path: ").strip()
    file = Path(file_path)

    if not file.exists():
        print("[!] File not found. Try again")
        return

    decrypt_password = input("[+] Enter password for decrypt: ")
    new_file_name = input("[+] Enter new file name: ")

    writer = PdfWriter()

    try:
        reader = PdfReader(file_path)
        if reader.is_encrypted:
            reader.decrypt(decrypt_password)

        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

        with open(new_file_name, 'wb') as file:
            writer.write(file)
    except Exception as e :
        print(f"[!] Error: {e}")

def main():
    choose = input("[+] Enter 0 for encrypt 1 for decrypt file: ").strip()
    match choose:
        case "1":
            decrypt()
        case "0":
            encrypt()
        case _:
            print("[!] Unknown command. Try again")

if __name__ == "__main__":
    main()
