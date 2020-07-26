import sys
import matplotlib
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        # self.canvas.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()
        self.show()

        # Create keys,
        self.push_button_day = QtWidgets.QPushButton("Day", self)
        self.push_button_week = QtWidgets.QPushButton("Week", self)
        self.push_button_month = QtWidgets.QPushButton("Month", self)
        self.push_button_total = QtWidgets.QPushButton("Total", self)

        # adding signals to push_buttons
        self.push_button_day.clicked.connect(self.update_data_day)
        self.push_button_week.clicked.connect(self.update_data_week)
        self.push_button_month.clicked.connect(self.update_data_month)
        self.push_button_total.clicked.connect(self.update_data_total)

        # Create layout for keys and plot
        self.layout_keys = QtWidgets.QVBoxLayout()
        self.layout_plot = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QHBoxLayout()

        # adding keys and plot to associated layouts
        self.layout_keys.addWidget(self.push_button_day)
        self.layout_keys.addWidget(self.push_button_week)
        self.layout_keys.addWidget(self.push_button_month)
        self.layout_keys.addWidget(self.push_button_total)
        self.layout_plot.addWidget(self.canvas)

        # creating main layout
        self.layout.addLayout(self.layout_keys)
        self.layout.addLayout(self.layout_plot)

        # Create a placeholder widget to hold our toolbar and canvas.
        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.show()

    def update_data_day(self):
        # sc = MplCanvas(self, width=5, height=4, dpi=100)
        # self.canvas.axes.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
        self.xdata = [0, 1, 2, 3, 4] #list(range(n_data))
        self.ydata = [0, 1, 4, 9, 16] #[random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

    def update_data_week(self):
        # sc = MplCanvas(self, width=5, height=4, dpi=100)
        # self.canvas.axes.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
        self.xdata = [0, 1, 2, 3, 4] #list(range(n_data))
        self.ydata = [0, 2, 8, 18, 32] #[random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

    def update_data_month(self):
        # sc = MplCanvas(self, width=5, height=4, dpi=100)
        # self.canvas.axes.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
        self.xdata = [0, 1, 2, 3, 4] #list(range(n_data))
        self.ydata = [0, 0.1, 0.4, 0.9, 0.16] #[random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

    def update_data_total(self):
        # sc = MplCanvas(self, width=5, height=4, dpi=100)
        # self.canvas.axes.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
        self.xdata = [0, 1, 2, 3, 4] #list(range(n_data))
        self.ydata = [0, 2, 0.5, 8, 23] #[random.randint(0, 10) for i in range(n_data)]
        self.update_plot()


    def update_plot(self):
        # Drop off the first y element, append a new one.
        # self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
