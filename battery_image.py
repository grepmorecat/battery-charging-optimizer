import tkinter as tk

class Battery_Image(object):
    '''Battery_Image Class creates an image of the battery and its percentage'''
    def __init__(self, root):
        '''
        self._root - root window of tkinter
        self._top_border - the border of the top of the battery image
        self._bottom_border - the border of the bottom of the battery image
        self._battery_cell_X - the layers of the battery
        '''
        self._root = root
        self._top_border = tk.Frame(self._root, relief=tk.GROOVE, border=1)
        self._bottom_border = tk.Frame(self._root, relief=tk.GROOVE, border=1)
        self._battery_cell_0 = tk.Frame(self._top_border)
        self._battery_cell_1 = tk.Frame(self._bottom_border)
        self._battery_cell_2 = tk.Frame(self._bottom_border)
        self._battery_cell_3 = tk.Frame(self._bottom_border)
        self._battery_cell_4 = tk.Frame(self._bottom_border)
        self._battery_cell_5 = tk.Frame(self._bottom_border)
        self._battery_cell_6 = tk.Frame(self._bottom_border)
        self._battery_cell_7 = tk.Frame(self._bottom_border)
        self._battery_cell_8 = tk.Frame(self._bottom_border)
        self._battery_cell_9 = tk.Frame(self._bottom_border)
        self.setSize()
        self.setGrid()

    def setSize(self):
        '''method creates the size of each cell in the battery'''
        self._battery_cell_0.configure(height=15, width=30)
        self._battery_cell_1.configure(height=15, width=70)
        self._battery_cell_2.configure(height=15, width=70)
        self._battery_cell_3.configure(height=15, width=70)
        self._battery_cell_4.configure(height=15, width=70)
        self._battery_cell_5.configure(height=15, width=70)
        self._battery_cell_6.configure(height=15, width=70)
        self._battery_cell_7.configure(height=15, width=70)
        self._battery_cell_8.configure(height=15, width=70)
        self._battery_cell_9.configure(height=15, width=70)

    def setGrid(self):
        '''method sets the location of the battery image on the tkinter frame'''
        self._battery_cell_0.grid(row=0, column=2)
        self._battery_cell_1.grid(row=1, column=2)
        self._battery_cell_2.grid(row=2, column=2)
        self._battery_cell_3.grid(row=3, column=2)
        self._battery_cell_4.grid(row=4, column=2)
        self._battery_cell_5.grid(row=5, column=2)
        self._battery_cell_6.grid(row=6, column=2)
        self._battery_cell_7.grid(row=7, column=2)
        self._battery_cell_8.grid(row=8, column=2)
        self._battery_cell_9.grid(row=9, column=2)
        self._top_border.grid(row=0, column=2, rowspan=3, padx=20)
        self._bottom_border.grid(row=0, column=2, rowspan=10, pady=32, padx=20)

    def interfaceBypassGrid(self):
        '''if in bypass mode change the position of the battery mode'''
        self._battery_cell_0.configure(height=15, width=30)
        self._top_border.grid(row=0, column=2, rowspan=5, padx=15, pady=20)

    def interfaceAutoGrid(self):
        '''if swapped back to auto mode swap the image back to original position'''
        self._battery_cell_0.configure(height=15, width=30)
        self._top_border.grid(row=0, column=2, rowspan=3, padx=20)

    def setCells(self, level):
        '''set the colours of the cells based on how much percentage the acutal battery has'''
        if (level >= 95):
            self._battery_cell_0.configure(background="lime")
            self._battery_cell_1.configure(background="lime")
            self._battery_cell_2.configure(background="lime")
            self._battery_cell_3.configure(background="lime")
            self._battery_cell_4.configure(background="lime")
            self._battery_cell_5.configure(background="lime")
            self._battery_cell_6.configure(background="lime")
            self._battery_cell_7.configure(background="lime")
            self._battery_cell_8.configure(background="lime")
            self._battery_cell_9.configure(background="lime")
        elif (level < 95 and level >= 85):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="lime")
            self._battery_cell_2.configure(background="lime")
            self._battery_cell_3.configure(background="lime")
            self._battery_cell_4.configure(background="lime")
            self._battery_cell_5.configure(background="lime")
            self._battery_cell_6.configure(background="lime")
            self._battery_cell_7.configure(background="lime")
            self._battery_cell_8.configure(background="lime")
            self._battery_cell_9.configure(background="lime")
        elif (level < 85 and level >= 75):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="white")
            self._battery_cell_2.configure(background="lime")
            self._battery_cell_3.configure(background="lime")
            self._battery_cell_4.configure(background="lime")
            self._battery_cell_5.configure(background="lime")
            self._battery_cell_6.configure(background="lime")
            self._battery_cell_7.configure(background="lime")
            self._battery_cell_8.configure(background="lime")
            self._battery_cell_9.configure(background="lime")
        elif (level < 75 and level >= 65):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="white")
            self._battery_cell_2.configure(background="white")
            self._battery_cell_3.configure(background="lime")
            self._battery_cell_4.configure(background="lime")
            self._battery_cell_5.configure(background="lime")
            self._battery_cell_6.configure(background="lime")
            self._battery_cell_7.configure(background="lime")
            self._battery_cell_8.configure(background="lime")
            self._battery_cell_9.configure(background="lime")
        elif (level < 65 and level >= 55):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="white")
            self._battery_cell_2.configure(background="white")
            self._battery_cell_3.configure(background="white")
            self._battery_cell_4.configure(background="lime")
            self._battery_cell_5.configure(background="lime")
            self._battery_cell_6.configure(background="lime")
            self._battery_cell_7.configure(background="lime")
            self._battery_cell_8.configure(background="lime")
            self._battery_cell_9.configure(background="lime")
        elif (level < 55 and level >= 45):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="white")
            self._battery_cell_2.configure(background="white")
            self._battery_cell_3.configure(background="white")
            self._battery_cell_4.configure(background="white")
            self._battery_cell_5.configure(background="lime")
            self._battery_cell_6.configure(background="lime")
            self._battery_cell_7.configure(background="lime")
            self._battery_cell_8.configure(background="lime")
            self._battery_cell_9.configure(background="lime")
        elif (level < 45 and level >= 35):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="white")
            self._battery_cell_2.configure(background="white")
            self._battery_cell_3.configure(background="white")
            self._battery_cell_4.configure(background="white")
            self._battery_cell_5.configure(background="white")
            self._battery_cell_6.configure(background="lime")
            self._battery_cell_7.configure(background="lime")
            self._battery_cell_8.configure(background="lime")
            self._battery_cell_9.configure(background="lime")
        elif (level < 35 and level >= 25):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="white")
            self._battery_cell_2.configure(background="white")
            self._battery_cell_3.configure(background="white")
            self._battery_cell_4.configure(background="white")
            self._battery_cell_5.configure(background="white")
            self._battery_cell_6.configure(background="white")
            self._battery_cell_7.configure(background="yellow")
            self._battery_cell_8.configure(background="yellow")
            self._battery_cell_9.configure(background="yellow")
        elif (level < 25 and level >= 15):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="white")
            self._battery_cell_2.configure(background="white")
            self._battery_cell_3.configure(background="white")
            self._battery_cell_4.configure(background="white")
            self._battery_cell_5.configure(background="white")
            self._battery_cell_6.configure(background="white")
            self._battery_cell_7.configure(background="white")
            self._battery_cell_8.configure(background="yellow")
            self._battery_cell_9.configure(background="yellow")
        elif (level < 15 and level >= 00):
            self._battery_cell_0.configure(background="white")
            self._battery_cell_1.configure(background="white")
            self._battery_cell_2.configure(background="white")
            self._battery_cell_3.configure(background="white")
            self._battery_cell_4.configure(background="white")
            self._battery_cell_5.configure(background="white")
            self._battery_cell_6.configure(background="white")
            self._battery_cell_7.configure(background="white")
            self._battery_cell_8.configure(background="white")
            self._battery_cell_9.configure(background="red")


