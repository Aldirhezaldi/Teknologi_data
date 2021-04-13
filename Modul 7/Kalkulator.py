import tkinter as tk


class Kalkulator:

    def __init__(self):
        self.__window = tk.Tk()
        self.__window.geometry('330x200')
        self.__window.title('Kalkulator')
        self.__init_widgets()

    def __init_widgets(self):
        print('Membuat widget-widget..')

        # Label dengan frame
        self.__frame_kiri = tk.Frame(master=self.__window, borderwidth=1)
        self.__lbl_b1 = tk.Label(master=self.__frame_kiri, text='Bilangan-1: ')
        self.__lbl_b2 = tk.Label(master=self.__frame_kiri, text='Bilangan-2: ')
        self.__lbl_hasil = tk.Label(master=self.__frame_kiri, text='Hasil: ')
        self.__lbl_b1.pack(pady=3)
        self.__lbl_b2.pack(pady=3)
        self.__lbl_hasil.pack(pady=3)
        self.__frame_kiri.grid(row=0, column=0, sticky='nw')

        # Textbox
        self.__frame_kanan = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__ent_b1 = tk.Entry(master=self.__frame_kanan, width=25)
        self.__ent_b2 = tk.Entry(master=self.__frame_kanan, width=25)
        self.__ent_hasil = tk.Entry(master=self.__frame_kanan, width=25)
        self.__ent_b1.pack()
        self.__ent_b2.pack()
        self.__ent_hasil.pack()
        self.__frame_kanan.grid(row=0, column=1, sticky='ne')

        # Button hitung
        self.__frame_bawah = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__btn_reset = tk.Button(master=self.__frame_bawah, text='Reset')
        self.__btn_tambah = tk.Button(master=self.__frame_bawah, text=' + ')
        self.__btn_kurang = tk.Button(master=self.__frame_bawah, text=' - ')
        self.__btn_kali = tk.Button(master=self.__frame_bawah, text=' * ')
        self.__btn_bagi = tk.Button(master=self.__frame_bawah, text=' / ')
        self.__btn_reset.pack(side=tk.LEFT)
        self.__btn_tambah.pack(side=tk.LEFT)
        self.__btn_kurang.pack(side=tk.LEFT)
        self.__btn_kali.pack(side=tk.LEFT)
        self.__btn_bagi.pack(side=tk.LEFT)
        self.__frame_bawah.grid(row=1, column=1, sticky='sw')

        # Bind action ke button
        self.__btn_reset.bind('<Button-1>', self.__on_btn_reset_left_click)
        self.__btn_tambah.bind('<Button-1>', self.__on_btn_tambah_left_click)
        self.__btn_kurang.bind('<Button-1>', self.__on_btn_kurang_left_click)
        self.__btn_kali.bind('<Button-1>', self.__on_btn_kali_left_click)
        self.__btn_bagi.bind('<Button-1>', self.__on_btn_bagi_left_click)

    # Action untuk button reset
    def __on_btn_reset_left_click(self, event: tk.Event):
        print('btn_reset click..')
        self.__ent_b1.delete(0, tk.END)
        self.__ent_b2.delete(0, tk.END)
        self.__ent_hasil.delete(0, tk.END)

    # Action untuk button hitung
    def __on_btn_tambah_left_click(self, event: tk.Event):
        print('btn_hitung click..')
        str_b1 = self.__ent_b1.get()
        str_b2 = self.__ent_b2.get()
        hasil = float(str_b1) + float(str_b2)
        self.__ent_hasil.delete(0, tk.END)
        self.__ent_hasil.insert(0, str(hasil))

    def __on_btn_kurang_left_click(self, event: tk.Event):
        print('btn_hitung click..')
        str_b1 = self.__ent_b1.get()
        str_b2 = self.__ent_b2.get()
        hasil = float(str_b1) - float(str_b2)
        self.__ent_hasil.delete(0, tk.END)
        self.__ent_hasil.insert(0, str(hasil))
    
    def __on_btn_kali_left_click(self, event: tk.Event):
        print('btn_hitung click..')
        str_b1 = self.__ent_b1.get()
        str_b2 = self.__ent_b2.get()
        hasil = float(str_b1) * float(str_b2)
        self.__ent_hasil.delete(0, tk.END)
        self.__ent_hasil.insert(0, str(hasil))
    
    def __on_btn_bagi_left_click(self, event: tk.Event):
        print('btn_hitung click..')
        str_b1 = self.__ent_b1.get()
        str_b2 = self.__ent_b2.get()
        hasil = float(str_b1) / float(str_b2)
        self.__ent_hasil.delete(0, tk.END)
        self.__ent_hasil.insert(0, str(hasil))

    def show(self):
        self.__window.mainloop()