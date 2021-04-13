import tkinter as tk
# Matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Pandas
import pandas as pd


class Diagram:

    def __init__(self):
        self.__window = tk.Tk()
        self.__window.geometry('600x400')
        self.__window.title('Diagram Negara VS GDP')
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
            'negara': ['USA', 'Canada', 'Germany', 'UK', 'France'],
            'gdp': [45000, 42000, 52000, 49000, 47000]
        }
        df = pd.DataFrame(data, columns=['negara', 'gdp'])
        return df

    def __gambar_plot(self, data: pd.DataFrame):
        # Figure
        figure = Figure(figsize=(6, 5), dpi=100)
        # Axes (Yang merender plot)
        axes = figure.add_subplot(1, 1, 1)
        axes.set_title('Negara Vs. GDP Per Kapita')
        # Gambar bar chart

        # Line
        #axes.plot(data['negara'], data['gdp'])

        # Bar
        #axes.bar(data['negara'], data['gdp'], color=['red', 'green', 'cyan', 'blue', 'gray'])

        # Scatter
        axes.scatter(data['negara'], data['gdp'], color=['red', 'green', 'cyan', 'blue', 'gray'])

        # Axes ditaruh di canvas
        canvas = FigureCanvasTkAgg(figure, self.__window)
        # Canvas dijadikan Widget Tkinter
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH)

    def show(self):
        self.__window.mainloop()
