import pandas as pd


class LatihanPandas:

    def __init__(self):
        self.data = None

    def tampilkan_pilihan(self):
        print('Latihan Pandas')
        print('--------------')
        print('Menu:')
        print('(1) Load dataset')
        print('(2) Tampilkan 5 baris teratas dan terakhir')
        print('(3) Tampilkan data grup riset sistem cerdas')
        print('(4) Tampilkan kolom nama pengusul dan judul proposal')
        print('(0) Keluar')
        pilihan = input('Pilihan Anda? ')
        if pilihan == '1':
            self.load_dataset()
            return True
        elif pilihan == '2':
            self.tampilkan_5_baris_awal_akhir()
            return True
        elif pilihan == '3':
            self.tampilkan_data_sistem_cerdas()
            return True
        elif pilihan == '4':
            self.tampilkan_pengusul_dan_judul()
            return True
        else:
            return False

    def load_dataset(self):
        self.data = pd.read_csv('files/rekap_proposal.csv',
                                sep=';', error_bad_lines=False, engine='python')
        self.data.set_index('id')
        print(self.data.to_string())

    def tampilkan_5_baris_awal_akhir(self):
        awal5 = self.data.head(5)
        print(awal5.to_string())
        akhir5 = self.data.tail(5)
        print(akhir5.to_string())

    def tampilkan_data_sistem_cerdas(self):
        print('SELEKSI baris dengan WHERE')
        self.data.sort_values('grup_riset', inplace=True)
        kondisi = self.data['grup_riset'] == 'SISTEM CERDAS'
        data_si = self.data.where(kondisi)
        print(data_si.to_string())

    def tampilkan_pengusul_dan_judul(self):
        nama = self.data['nama_pengusul']
        judul = self.data.judul_proposal
        gabung_baris = pd.concat([nama, judul], axis=0)
        print(gabung_baris.to_string())
        gabung_kolom = pd.concat([nama, judul], axis=1)
        print(gabung_kolom.to_string())

