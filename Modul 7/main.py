from HelloGUI import HelloGUI
from Diagram import  Diagram
from Kalkulator import Kalkulator

class Main:
    @staticmethod
    def main():
        main_window = HelloGUI()
        main_window = Diagram()
        # main_window = Kalkulator()
        main_window.show()

Main.main()