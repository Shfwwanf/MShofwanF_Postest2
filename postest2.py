from prettytable import PrettyTable

# Definisikan kelas TokoHotWheels
class TokoHotWheels:
    # Konstruktor untuk inisialisasi toko
    def __init__(self):
        # Data barang-barang yang dijual di toko
        self.barang = [
            {'nama': 'Hot Wheels Regular', 'harga': 33000.0, 'stok': 25},
            {'nama': 'Hot Wheels Premium', 'harga': 115000.0, 'stok': 8},
            {'nama': 'Hot Wheels Fast&Furious Regular', 'harga': 55000.0, 'stok': 6},
            {'nama': 'Hot Wheels Team Transport', 'harga': 230000.0, 'stok': 3},
            {'nama': 'Hot Wheels Fast&Furious 5 Cars Premium', 'harga': 475000.0, 'stok': 1},
        ]
        # Data pembeli dan transaksi pembeli
        self.pembeli = []
        self.transaksi_pembeli = []
        # Data admin untuk login
        self.admin = {
            'username': 'wawan',
            'password': 'wawangantenk'
        }
        # Pengguna yang sedang login
        self.logged_in_user = None

    # Fungsi untuk login
    def login(self, username, password):
        if username == self.admin['username'] and password == self.admin['password']:
            self.logged_in_user = 'wawan'
            print("Selamat datang, Yang Mulia Admin Wawan!")
        else:
            if username == self.admin['username']:
                print("Password admin salah bang!")
            else:
                self.logged_in_user = 'pembeli'
                print(f"Selamat datang, {username}!")

    # Fungsi untuk menambahkan barang (hanya admin yang dapat)
    def tambah_barang(self, nama, harga, stok):
        if self.logged_in_user == 'wawan':
            self.barang.append({'nama': nama, 'harga': harga, 'stok': stok})
            print(f"Barang {nama} dengan stok {stok} telah ditambahkan.")
        else:
            print("Anda tidak memiliki izin untuk menambahkan barang.")

    # Fungsi untuk melihat daftar barang
    def lihat_barang(self):
        if len(self.barang) > 0:
            print("\n")
            table = PrettyTable()
            table.field_names = ["No", "Nama Barang", "Harga", "Stok"]
            for i, item in enumerate(self.barang, 1):
                table.add_row([i, item['nama'], item['harga'], item['stok']])
            print(table)
            print("\n")
        else:
            print("Tidak ada barang dalam daftar.")

    # Fungsi untuk mengupdate informasi barang (hanya admin yang dapat)
    def update_barang(self, nomor_barang, nama_baru, harga_baru, stok_baru):
        if self.logged_in_user == 'wawan':
            if 0 < nomor_barang <= len(self.barang):
                barang = self.barang[nomor_barang - 1]
                barang['nama'] = nama_baru
                barang['harga'] = harga_baru
                barang['stok'] = stok_baru
                print("Barang telah diperbarui.")
            else:
                print("Nomor barang tidak valid.")
        else:
            print("Anda tidak memiliki izin untuk mengupdate barang.")

    # Fungsi untuk menghapus barang (hanya admin yang dapat)
    def hapus_barang(self, nomor_barang):
        if self.logged_in_user == 'wawan':
            if 0 < nomor_barang <= len(self.barang):
                deleted_item = self.barang.pop(nomor_barang - 1)
                print(f"Barang '{deleted_item['nama']}' telah dihapus.")
            else:
                print("Nomor barang tidak valid.")
        else:
            print("Anda tidak memiliki izin untuk menghapus barang.")

    # Fungsi untuk pembelian barang (hanya pembeli yang dapat)
    def beli_barang(self, nomor_barang, jumlah):
        if self.logged_in_user == 'pembeli':
            if 0 < nomor_barang <= len(self.barang):
                barang = self.barang[nomor_barang - 1]
                if barang['stok'] >= jumlah:
                    total_harga = barang['harga'] * jumlah
                    nama_pembeli = input("> Nama Anda          : ")
                    nomor_pembeli = input("> Nomor telepon Anda : ")
                    alamat_pembeli = input("> Alamat Anda        : ")
                    metode_pembayaran = input("> Metode pembayaran  : ")
                    self.transaksi_pembeli.append({
                        'nama_pembeli': nama_pembeli,
                        'nomor_pembeli': nomor_pembeli,
                        'alamat_pembeli': alamat_pembeli,
                        'metode_pembayaran': metode_pembayaran,
                        'barang_dibeli': barang['nama'],
                        'jumlah': jumlah,
                        'total_harga': total_harga
                    })
                    barang['stok'] -= jumlah
                    print(52*"_")
                    print("                   -- Transaksi --")
                    print(52*"-")
                    print("\n")
                    print(f"Nama Pembeli        : {nama_pembeli}")
                    print(f"Nomor Hp            : {nomor_pembeli}")
                    print(f"Alamat              : {alamat_pembeli}")
                    print(f"Barang              : {barang['nama']}")
                    print(f"Harga               : {total_harga}")
                    print(f"Metode Pembayaran   : {metode_pembayaran}")
                    print("\n")
                    print(f"Terima kasih, {nama_pembeli}! Pembayaran anda sudah Diverifikasi.")
                    print(f"Anda telah membeli {jumlah} {barang['nama']} seharga {total_harga}.")
                    print(f"Pesanan Anda akan dikirimkan ke alamat anda.")
                else:
                    print(f"Stok {barang['nama']} tidak mencukupi.")
            else:
                print("Nomor barang tidak valid.")
        else:
            print("Anda tidak memiliki izin untuk melakukan transaksi.")

    # Fungsi untuk logout dari akun
    def logout(self):
        self.logged_in_user = None
        print("Anda telah keluar.")

# Fungsi utama program
def main():
    # Inisialisasi toko
    toko = TokoHotWheels()

    while True:
        print(52*"=")
        print("          <<<<< SELAMAT DATANG WEEEEEE >>>>>")
        print("              << SPEEDY WHEELS HEAVEN >>")
        print(52*"=")
        print("                 -- Silahkan Login --")
        print(52*"-")
        print("\n")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Pembeli")
        print("3. Keluar")
        pilihan = input("> Pilih peran atau keluar : ")

        if pilihan == '1':
            # Login sebagai admin
            username = input(" > Masukkan username : ")
            password = input(" > Masukkan password : ")
            toko.login(username, password)

            if toko.logged_in_user == 'wawan':
                while True:
                    print(52*"_")
                    print("                   -- Menu Admin --")
                    print(52*"-")
                    print("\n")
                    print("1. Tambah Barang")
                    print("2. Lihat Barang")
                    print("3. Hapus Barang")
                    print("4. Update Barang")
                    print("5. Logout")
                    admin_pilihan = input("> Pilih opsi : ")
                    print(52*"_")

                    if admin_pilihan == '1':
                        # Menambahkan barang baru
                        nama_barang = input(" > Masukkan nama barang : ")
                        harga_barang = float(input(" > Masukkan harga barang : "))
                        stok_barang = int(input(" > Masukkan stok barang : "))
                        toko.tambah_barang(nama_barang, harga_barang, stok_barang)
                    elif admin_pilihan == '2':
                        # Melihat daftar barang
                        toko.lihat_barang()
                    elif admin_pilihan == '3':
                        # Melihat daftar barang dan menghapus salah satu
                        toko.lihat_barang()
                        nomor_barang = int(input(" > Pilih nomor barang yang ingin dihapus : "))
                        toko.hapus_barang(nomor_barang)
                    elif admin_pilihan == '4':
                        # Melihat daftar barang dan mengupdate salah satu
                        toko.lihat_barang()
                        nomor_barang = int(input(" > Pilih nomor barang yang ingin diupdate : "))
                        nama_baru = input(" > Masukkan nama baru : ")
                        harga_baru = float(input(" > Masukkan harga baru : "))
                        stok_baru = int(input(" > Masukkan stok baru : "))
                        toko.update_barang(nomor_barang, nama_baru, harga_baru, stok_baru)
                    elif admin_pilihan == '5':
                        # Logout dari akun admin
                        toko.logout()
                        break
                    else:
                        print("Opsi tidak valid.")

        elif pilihan == '2':
            # Login sebagai pembeli
            username = input(" > Masukkan Nama anda : ")
            password = input(" > Masukkan password  : ")
            toko.login(username, password)

            if toko.logged_in_user == 'pembeli':
                while True:
                    print(52*"_")
                    print("                   -- Menu Pembeli --")
                    print(52*"-")
                    print("\n")
                    print("1. Beli Barang")
                    print("2. Logout")
                    pembeli_pilihan = input("> Pilih opsi : ")
                    print(52*"_")

                    if pembeli_pilihan == '1':
                        # Melihat daftar barang dan melakukan pembelian
                        toko.lihat_barang()
                        nomor_barang = int(input("> Nomor Barang yang ingin dibeli : "))
                        jumlah_barang = int(input("> Jumlah barang yang ingin dibeli: "))
                        toko.beli_barang(nomor_barang, jumlah_barang)
                    elif pembeli_pilihan == '2':
                        # Logout dari akun pembeli
                        toko.logout()
                        break
                    else:
                        print("Opsi tidak valid.")

        elif pilihan == '3':
            # Keluar dari program
            print(52*"=")
            print("         <<<<< MKSH TELAH BERBELANJA DI >>>>>")
            print("              << SPEEDY WHEELS HEAVEN >>")
            print(52*"=")
            break
        else:
            print("Opsi tidak valid.")

# Memulai program
if __name__ == "__main__":
    main()
