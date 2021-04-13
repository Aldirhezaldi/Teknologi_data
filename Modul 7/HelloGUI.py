import tkinter as tk

class HelloGUI:
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title('Hello, GUI!')
        self.__init_widgets()

    def __init_widgets(self):
        # Buat widgets
        self.__ent_nama = tk.Entry(master=self.__window)
        self.__btn_aksi = tk.Button(master=self.__window, text='Klik Saya!')
        self.__lbl_halo = tk.Label(master=self.__window, text='Hello, World!')
        # Pack!
        self.__ent_nama.pack()
        self.__btn_aksi.pack()
        self.__lbl_halo.pack()
        # Bind event
        self.__btn_aksi.bind('<Button-1>', self.__on_btn_aksi_left_click)
    def __on_btn_aksi_left_click(self, event: tk.Event):
        nama = self.__ent_nama.get()
        salam = "Halo, {}! Selamat datang di Tkinter.. :)".format(nama)
        self.__lbl_halo['text'] = salam
    def show(self):
        self.__window.mainloop()