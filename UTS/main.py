from Bar import  Bar
from scatter import scatter
from Line import Line

class Main:
    @staticmethod
    def main():
        main_window = scatter()
        main_window = Line()
        main_window = Bar()
        main_window.show()

Main.main()
