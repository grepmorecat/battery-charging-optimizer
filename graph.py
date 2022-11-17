'''Create a class and use tkinter to create a window that displays an icon that is a line graph with the x-axis representing the time and the y-axis representing the power level
'''
import tkinter
from tkinter import *
from tkinter import ttk


class Graph(tkinter.Canvas):
    def __init__(self, master, width, height, bg, x_axis, y_axis, x_title, y_title, title, data):
        tkinter.Canvas.__init__(self, master, width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.bg = bg
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_title = x_title
        self.y_title = y_title
        self.title = title
        self.data = data
        self.create_graph()

    def create_graph(self):
        # self.create_rectangle(0, 0, self.width, self.height, fill=self.bg)
        # y坐标轴
        self.create_line(50, 50, 50, self.height - 50, width=2)
        # x坐标轴
        self.create_line(50, self.height - 50, self.width - 50, self.height - 50, width=2)
        # text
        self.create_text(50, 25, text=self.title, anchor=tkinter.W)
        # y轴text
        self.create_text(20, self.height - 370, text=self.y_title, anchor=tkinter.W)
        # x轴text
        self.create_text(self.width - 50, self.height - 15, text=self.x_title, anchor=tkinter.W)
        self.create_text(self.width - 25, 50, text='monitor', anchor=tkinter.E)
        self.create_text(self.width / 2, 25, text='Battery level Graph', anchor=tkinter.CENTER)

        # Draw the x-axis labels

        x_step = (self.width - 100) / self.x_axis
        for i in range(0, self.x_axis + 1):
            self.create_line(50 + i * x_step, self.height - 50, 50 + i * x_step, self.height - 45, width=2)
            self.create_text(50 + i * x_step, self.height - 35, text=str(i), anchor=tkinter.N)

        # Draw the y-axis labels
        y_step = (self.height - 100) / self.y_axis
        for i in range(0, self.y_axis + 1):
            self.create_line(50, self.height - 50 - i * y_step, 45, self.height - 50 - i * y_step, width=2)
            self.create_text(35, self.height - 50 - i * y_step, text=str(i), anchor=tkinter.E)

        # Draw the data
        for i in range(0, len(self.data)):
            x = 50 + i * x_step
            y = self.height - 50 - self.data[i] * y_step
            self.create_oval(x - 2, y - 2, x + 2, y + 2, fill='red', outline='red')
            if i > 0:
                self.create_line(50 + (i - 1) * x_step, self.height - 50 - self.data[i - 1] * y_step, x, y, width=2,
                                 fill='red')


root = tkinter.Tk()
root.title('Graph')
root.geometry('600x400')
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 19, 19, 20]
graph = Graph(root, 600, 400, 'white', 20, 20, 'Time', 'Level', 'Power Level over Time', data)
graph.pack()
root.mainloop()








