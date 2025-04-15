from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, errors

import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

import ttkbootstrap as tb
from ttkbootstrap import  Querybox
from ttkbootstrap.dialogs import Messagebox


def encrypt(file_path,password):
    file = Path(file_path)

    if not file.exists():
        print('[!] File not exist in given path. Try again')
        return

    new_file_name = f"encrypted_{file.name}"
    reader = PdfReader(file_path)
    writer = PdfWriter()

    for page in range(len(reader.pages)):
        writer.add_page(reader.pages[page])

    writer.encrypt(password)

    print(f"[*] Writing to {new_file_name}...")
    with open(new_file_name,'wb') as file:
        writer.write(file)
        print(f"[+] Created {new_file_name}")
        Messagebox.ok("File encrypted successfully!", title="Success", alert=True)


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
        messagebox.showinfo("Success", f"File: {file_path}\nPassword: {password}", parent=window)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[('PDF','.pdf')])
    if file_path:
        password = Querybox.get_string("Enter password for encryption", title="Password")
        if password:

            encrypt(file_path, password)

def main():
    window.title("Encrypt && Decrypt PDF")
    window.geometry('400x200')

    btn = tb.Button(
        window,
        text="Select File to Encrypt",
        bootstyle="primary",  # Correct bootstyle usage
        width=30,
        command=select_file,
        padding=(10, 15),
    )
    btn.pack(expand=True)

    window.mainloop()

window = tk.Tk()
if __name__ == "__main__":
    main()
