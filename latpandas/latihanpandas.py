import pandas as pd


class Latihanpandas:
    def __init__(self):
        self.data = None

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
