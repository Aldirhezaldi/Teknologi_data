from app import App

class Main:

    @staticmethod
    def main():
        app = App()
        selesai = False
        while selesai is not True:
            selesai = app.jalankan()


Main.main()