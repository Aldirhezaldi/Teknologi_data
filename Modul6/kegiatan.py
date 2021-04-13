from datetime import datetime


class Kegiatan:
    def __init__(self):
        self.tanggal = datetime.now()
        self.nama = ''
        self.tersimpan = []

    def tampilkan_form(self):
        str_tanggal = input('Masukkan Tanggal: ')
        str_nama = input('Masukkan Nama: ')
        self.tanggal = datetime.strptime(str_tanggal, '%Y-%m-%d')
        self.nama = str_nama

    def simpan(self):
        data = {'tanggal': self.tanggal, 'nama': self.nama}
        self.tersimpan.append(data)

    def tampilkan_tersimpan(self):
        i = 0
        while i < len(self.tersimpan):
            baris = self.tersimpan[i]
            print('{}. [{}] {}'.format((i + 1), baris['tanggal'], baris['nama']))
            i = (i + 1)

