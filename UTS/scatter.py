import tkinter as tk
# Matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Pandas
import pandas as pd


class scatter:

    def __init__(self):
        self.__window = tk.Tk()
        self.__window.geometry('1500x400')
        self.__window.title('Top Rated Movies IMDb')
        # Gambar widget-widget di Window
        self.__init_widgets()

    def __init_widgets(self):
        data = self.get_data()
        self.__frame_atas = tk.Frame(master=self.__window, borderwidth=1, relief=tk.RAISED)
        self.__gambar_plot(data)

    def get_data(self):
        # Data, pada contoh ini hardcode.
        # Riilnya data bisa didapat dari file atau database atau web API, atau yang lainnya..
        data = {
            'movies': ['Zack Snyders Justice League', 'The Godfather', 'The Dark Knight', 'The Godfather: Part II', '12 Angry Men'],
            'rating': [8.0, 10.0, 9.5, 8.5, 7.0]
        }
        df = pd.DataFrame(data, columns=['movies', 'rating'])
        return df

    def __gambar_plot(self, data: pd.DataFrame):
        # Figure
        figure = Figure(figsize=(20, 5), dpi=100)
        # Axes (Yang merender plot)
        axes = figure.add_subplot(1, 1, 1)
        axes.set_title('Top Movies Rated IMDb')
        # Gambar bar chart



        # Scatter
        axes.scatter(data['movies'], data['rating'], color=['red', 'orange', 'yellow', 'green', 'blue'])

        # Axes ditaruh di canvas
        canvas = FigureCanvasTkAgg(figure, self.__window)
        # Canvas dijadikan Widget Tkinter
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH)

    def show(self):
        self.__window.mainloop()
