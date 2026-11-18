import inquirer
import pungsi as p
from menu_admin import menu_admin
from menu_user import menu_user
daftar_user_baru = []

p.bersihkan_layar()
while p.current_role is None:
    print('='*22, "Selamat datang!", "="*22)    
    tanya_awal = [
        inquirer.List(
            "pilihan_awal",
            message="Masukkan pilihan",
            choices=["1. Login", "2. Register", "3. Keluar"],
        )
    ]
    jawab_awal = inquirer.prompt(tanya_awal)
    pilihan = jawab_awal["pilihan_awal"]
    
    if "2." in pilihan:
        p.bersihkan_layar()
        print('='*22, 'LAMAN REGISTER', '='*22)
        
        # Validasi Username: Wajib string, tidak boleh kosong, tidak boleh duplikat
        while True:
            new_user = input('Buat Username: ')
            
            if new_user == "":
                print("Error: Username tidak boleh kosong!")
                continue
                
            # Cek apakah username sudah ada di database sementara
            username_sudah_ada = False
            for akun in daftar_user_baru:
                if akun[0] == new_user:
                    username_sudah_ada = True
                    break
            
            if username_sudah_ada:
                print(f"Error: Username '{new_user}' sudah terdaftar! Gunakan username lain.")
            else:
                break
            
        # Validasi Password: Wajib angka, tidak boleh kosong, TANPA isdigit()
        while True:
            new_pass = input('Buat Password (Wajib berupa angka): ')
            
            if new_pass == "":
                print("Error: Password tidak boleh kosong!")
                continue
                
            # Cek apakah bisa diubah ke integer tanpa pakai isdigit()
            try:
                int(new_pass)
                break # Kalau berhasil diubah ke angka, berarti valid
            except ValueError:
                print("Error: Password harus berupa angka!")
            
        # Simpan ke database sementara (list)
        daftar_user_baru.append([new_user, new_pass])
            
        print("Registrasi berhasil! Silahkan login kembali.")
        input("Tekan Enter untuk melanjutkan...")
        p.bersihkan_layar()

    # --- MENU LOGIN ---
    elif "1." in pilihan:
        
        p.bersihkan_layar()
        print('='*22, 'LOGIN', '='*22)
        usn_login = input('Masukkan Username: ')
        pw_login = input('Masukkan Password: ')
        
        # Cek apakah cocok dengan salah satu admin di pungsi.py
        is_admin_found = False
        for adm in p.daftar_admin:
            if usn_login == adm[0] and pw_login == adm[1]:
                is_admin_found = True
                break
        
        if is_admin_found:
            p.bersihkan_layar()
            print('='*22, 'Login Admin berhasil.', '='*22)
            p.current_role = "admin"
            menu_admin()
            
        else:
            # Cek apakah cocok dengan user di database sementara (list)
            user_ditemukan = False
            for akun in daftar_user_baru:
                if usn_login == akun[0] and pw_login == akun[1]:
                    user_ditemukan = True
                    break
            
            if user_ditemukan:
                p.bersihkan_layar()
                print('='*22, 'Login User berhasil.', '='*22)
                p.current_role = "user"
                menu_user()
            else:
                p.bersihkan_layar()
                print('Username atau Password salah atau tidak terdaftar! Silahkan coba lagi.')
                input("Tekan Enter untuk melanjutkan...")
                p.bersihkan_layar()
                
    # --- MENU KELUAR ---
    else: 
        print("Keluar dari program. Terima kasih!")
        break