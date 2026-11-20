import inquirer
import pungsi as p
from menu_admin import menu_admin
from menu_user import menu_user

data_akun = []

username_admin = ["Rizki", "Surya", "Rizal"]
password_admin = ["007", "002", "001"]
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
        p.bersihkan_layar()
        print("=" * 22, "LAMAN REGISTER", "=" * 22)

        while True:
            username = input("Buat Username: ")
            password = input("Buat Password: ")

            try:
                int(password)
                password_angka = True
            except ValueError:
                password_angka = False

            if type(username) != str or password_angka == False:
                print("Username harus berupa teks dan password harus berupa angka!")
                continue

            if username == "" or password == "":
                print("Username dan Password tidak boleh kosong!")
                continue

            sudah_ada = False
            for akun in data_akun:
                if akun[0] == username:
                    sudah_ada = True

            if sudah_ada == True:
                print("Username sudah terdaftar!")
                continue

            data_akun.append([username, password])
            print("Register berhasil! Silakan login kembali.")
            input("Tekan Enter untuk melanjutkan...")
            p.bersihkan_layar()
            break

    # ---------- LOGIN ----------
    elif "1." in pilihan:
        p.bersihkan_layar()
        print("=" * 22, "LOGIN", "=" * 22)

        login2 = False
        while login2 != True:
            usn_login = input("Masukkan Username: ")
            pw_login = input("Masukkan Password: ")

            user_cocok = False
            for akun in data_akun:
                if usn_login == akun[0] and pw_login == akun[1]:
                    user_cocok = True

            if user_cocok == True:
                print("Login berhasil!")
                p.loginuser = True
                login2 = True
                p.login = True
            else:
                admin_cocok = False
                for i in range(len(username_admin)):
                    if usn_login == username_admin[i] and pw_login == password_admin[i]:
                        admin_cocok = True

                if admin_cocok == True:
                    p.login = True
                    login2 = True
                    p.loginadmin = True
                else:
                    print("Username atau Password salah atau tidak terdaftar! Silakan coba lagi.")
                    input("Tekan Enter untuk melanjutkan...")
                    p.bersihkan_layar()
                    break  # balik ke menu awal

        if p.loginadmin == True:
            menu_admin()
        elif p.loginuser == True:
            menu_user()

    # ---------- KELUAR ----------
    else:
        break