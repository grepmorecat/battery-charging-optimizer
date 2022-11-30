import tkinter as tk

class Labels(object):
    def __init__(self, root, battery):
        self._root = root
        self._battery = battery
        tk.Label(self._root, text="Battery Level: ", font=15).grid(row=0, column=0)
        self._selectedMode = tk.StringVar()
        self._selectedMode.set("Auto")
        tk.Label(self._root, text="Current Mode:", font=15).grid(row=2, column=0)
        tk.Label(self._root, textvariable=self._selectedMode, font=15).grid(row=2, column=1)


        self._selected = tk.IntVar()
        self._label1 = tk.Label(self._root, text="Setting Threshold to: ", font=15)
        self._label2 = tk.Label(self._root, textvariable=self._selected, font=15)


        self._level = tk.StringVar()
        self._level.set(self._battery.getLevel())
        self._labelBattery = tk.Label(self._root, textvariable=self._level, font=15)
        self._labelBattery.grid(row=0, column=1)
        self.loadBatteryLevel()

    def loadBatteryLevel(self):
        self._level.set(self._battery.getLevel())
        self._labelBattery.config(textvariable=self._level)
        self._labelBattery.after(1000, self.loadBatteryLevel)


    def setSelected(self, selected):
        self._selected.set(selected)


    def deleteLabelsForThreshold(self):
        self._label1.grid_remove()
        self._label2.grid_remove()

    def createLabelsForThreshold(self):
        self._label1.grid(row=4, column=0)
        self._label2.grid(row=4, column=1)
        self.setSelected(100)

    def setSelectedMode(self, mode):
        self._selectedMode.set(mode)