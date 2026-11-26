import os
import inquirer
import pungsi as p
from menu_admin import menu_admin
from menu_user import menu_user

BATAS_PERCOBAAN = 3

os.system("cls" if os.name == "nt" else "clear")
while True:
    print("=" * 22, "Selamat datang!", "=" * 22)
    tanya_awal = inquirer.prompt([
        inquirer.List(
            "pilihan_awal",
            message="Masukkan pilihan",
            choices=["1. Login", "2. Register", "3. Keluar"],
        )
    ])
    if tanya_awal is None or "3." in tanya_awal["pilihan_awal"]:
        break

    pilihan = tanya_awal["pilihan_awal"]

    if "2." in pilihan:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 22, "LAMAN REGISTER", "=" * 22)
            print("Ketik 0 pada username untuk kembali ke menu awal.")

            username = input("Buat Username: ").strip()
            if username == "0":
                os.system("cls" if os.name == "nt" else "clear")
                break
            if username == "":
                print("Username tidak boleh kosong!")
                input("Tekan Enter untuk mengulang...")
                continue
            if username.isdigit():
                print("Username harus berupa teks, tidak boleh angka saja!")
                input("Tekan Enter untuk mengulang...")
                continue

            sudah_ada = False
            for adm in p.daftar_admin:
                if username.lower() == adm[0].lower():
                    sudah_ada = True
            for akun in p.data_akun:
                if username.lower() == akun[0].lower():
                    sudah_ada = True

            if sudah_ada == True:
                print("Username sudah terdaftar!")
                input("Tekan Enter untuk mengulang...")
                continue

            password = input("Buat Password (hanya angka): ")

            if password == "":
                print("Password tidak boleh kosong!")
                input("Tekan Enter untuk mengulang...")
                continue

            if not password.isdigit():
                print("Password harus berupa angka!")
                input("Tekan Enter untuk mengulang...")
                continue

            p.data_akun.append([username, password, False])
            p.simpan_data_akun(p.data_akun)
            print("Register berhasil! Silakan login kembali.")
            input("Tekan Enter untuk melanjutkan...")
            os.system("cls" if os.name == "nt" else "clear")
            break

    elif "1." in pilihan:
        percobaan = 0
        login = False
        batal_login = False
        p.loginadmin = False
        p.loginuser = False
        p.akun_login = ""

        while login != True and percobaan < BATAS_PERCOBAAN:
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 22, "LOGIN", "=" * 22)
            print(f"Percobaan ke-{percobaan + 1} dari {BATAS_PERCOBAAN}")
            print("Ketik 0 pada username untuk kembali ke menu awal.")

            usn_login = input("Masukkan Username: ").strip()
            if usn_login == "0":
                batal_login = True
                break

            pw_login = input("Masukkan Password: ").strip()

            username_ada = False
            akun_dibanned = False

            for akun in p.data_akun:
                if usn_login.lower() == akun[0].lower():
                    username_ada = True
                    if akun[2] == True:
                        akun_dibanned = True
                    elif pw_login == akun[1]:
                        p.loginuser = True
                        p.akun_login = akun[0]
                        login = True
                    break

            if login != True:
                for adm in p.daftar_admin:
                    if usn_login.lower() == adm[0].lower():
                        username_ada = True
                        if pw_login == adm[1]:
                            p.loginadmin = True
                            login = True
                        break

            if login == True:
                print("Login berhasil!")
                input("Tekan Enter untuk melanjutkan...")
                input("Tekan Enter untuk melanjutkan...")
            else:
                percobaan += 1
                if akun_dibanned == True:
                    print("Akun ini sedang di-BANNED oleh admin!")
                elif username_ada == True:
                    print("Password salah!")
                else:
                    print("Akun belum terdaftar!")
                input("Tekan Enter untuk melanjutkan...")
                    print("Akun belum terdaftar!")
                input("Tekan Enter untuk melanjutkan...")

        if p.loginadmin:
            menu_admin()
        elif p.loginuser:
            menu_user()
        elif percobaan >= BATAS_PERCOBAAN:
            print("Percobaan login habis. Kembali ke menu awal.")
            input("Tekan Enter untuk melanjutkan...")

        p.loginadmin = False
        p.loginuser = False
        p.akun_login = ""
        os.system("cls" if os.name == "nt" else "clear")