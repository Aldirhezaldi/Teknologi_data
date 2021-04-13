from kegiatan import Kegiatan
# from keuangan import Keuangan
from latihanpandas.latihanpandas import LatihanPandas


class App:
    def __init__(self):
        self.kegiatan = Kegiatan()

    def jalankan(self):
        print('------------------------------')
        print('Selamat datang di PencatatApp!')
        print('------------------------------')
        print('Menu:')
        print('(1) Input catatan baru')
        print('(2) Lihat catatan tersimpan')
        print('(3) Latihan Pandas')
        print('(0) Keluar')
        pilihan = input('Pilihan Anda? ')
        if pilihan == '0':
            selesai = True
        else:
            if pilihan == '1':
                self.kegiatan.tampilkan_form()
                self.kegiatan.simpan()
            elif pilihan == '2':
                self.kegiatan.tampilkan_tersimpan()
            elif pilihan == '3':
                print('Membuka program latihan Pandas')
                lp = LatihanPandas()
                lanjut = True
                while lanjut:
                    lanjut = lp.tampilkan_pilihan()
            else:
                print('[ERROR] Pilihan tidak valid!')
            selesai = False
        return selesai
