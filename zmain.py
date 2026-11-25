import inquirer
import pungsi as p
from menu_admin import menu_admin
from menu_user import menu_user

data_akun = []
batas_percobaan = 3

p.bersihkan_layar()

while p.login != True:
    print("=" * 22, "Selamat datang!", "=" * 22)
    tanya_awal = [
        inquirer.List(
            "pilihan_awal",
            message="Masukkan pilihan",
            choices=["1. Login", "2. Register", "3. Keluar"],
        )
    ]
    jawab_awal = inquirer.prompt(tanya_awal)
    if jawab_awal == None:
        break
    pilihan = jawab_awal["pilihan_awal"]

    # ---------- REGISTER ----------
    if "2." in pilihan:
        while True:
            p.bersihkan_layar()
            print("=" * 22, "LAMAN REGISTER", "=" * 22)
            print("Ketik 0 pada username untuk kembali ke menu awal.")

            username = input("Buat Username: ")

            if username == "0":
                p.bersihkan_layar()
                break

            # 1. Cek username langsung setelah diinput
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
            for akun in data_akun:
                if username.lower() == akun[0].lower():
                    sudah_ada = True

            if sudah_ada == True:
                print("Username sudah terdaftar!")
                input("Tekan Enter untuk mengulang...")
                continue

            # 2. Baru minta password setelah username lolos
            tanya_pw = [inquirer.Password("password", message="Buat Password")]
            jawab_pw = inquirer.prompt(tanya_pw)
            if jawab_pw == None:
                p.bersihkan_layar()
                break
            password = jawab_pw["password"]

            if password == "":
                print("Password tidak boleh kosong!")
                input("Tekan Enter untuk mengulang...")
                continue

            if not password.isdigit():
                print("Password harus berupa angka!")
                input("Tekan Enter untuk mengulang...")
                continue

            # 3. Konfirmasi password
            tanya_konfirmasi = [inquirer.Password("konfirmasi", message="Ulangi Password")]
            jawab_konfirmasi = inquirer.prompt(tanya_konfirmasi)
            if jawab_konfirmasi == None:
                p.bersihkan_layar()
                break

            if jawab_konfirmasi["konfirmasi"] != password:
                print("Konfirmasi password tidak sama!")
                input("Tekan Enter untuk mengulang...")
                continue

            data_akun.append([username, password])
            print("Register berhasil! Silakan login kembali.")
            input("Tekan Enter untuk melanjutkan...")
            p.bersihkan_layar()
            break

    # ---------- LOGIN ----------
    elif "1." in pilihan:
        percobaan = 0

        while p.login != True and percobaan < batas_percobaan:
            p.bersihkan_layar()
            print("=" * 22, "LOGIN", "=" * 22)
            print(f"Percobaan ke-{percobaan + 1} dari {batas_percobaan}")

            usn_login = input("Masukkan Username: ")
            tanya_pw = [inquirer.Password("password", message="Masukkan Password")]
            jawab_pw = inquirer.prompt(tanya_pw)
            if jawab_pw == None:
                break
            pw_login = jawab_pw["password"]

            username_ada = False

            # Cek akun user (username tidak membedakan huruf besar/kecil)
            for akun in data_akun:
                if usn_login.lower() == akun[0].lower():
                    username_ada = True
                    if pw_login == akun[1]:
                        p.loginuser = True
                        p.akun_login = akun[0]
                        p.login = True

            # Cek akun admin
            if p.login != True:
                for adm in p.daftar_admin:
                    if usn_login.lower() == adm[0].lower():
                        username_ada = True
                        if pw_login == adm[1]:
                            p.loginadmin = True
                            p.login = True

            if p.login == True:
                print("Login berhasil!")
                input("Tekan Enter untuk melanjutkan...")
            else:
                percobaan += 1
                if username_ada == True:
                    print("Password salah!")
                else:
                    print("Akun belum terdaftar!")
                input("Tekan Enter untuk melanjutkan...")

        if p.loginadmin == True:
            menu_admin()
        elif p.loginuser == True:
            menu_user()
        elif percobaan >= batas_percobaan:
            print("Percobaan login habis. Kembali ke menu awal.")
            input("Tekan Enter untuk melanjutkan...")

        # Reset status supaya kembali ke menu awal setelah logout
        p.login = False
        p.loginadmin = False
        p.loginuser = False
        p.akun_login = ""
        p.bersihkan_layar()

    # ---------- KELUAR ----------
    else:
        break