import tkinter as tk
from tkinter import ttk
from labels import Labels
from graph import Graph
from battery_simulated import Battery
from tracker import Tracker

class GUI(object):
    def __init__(self, battery: Battery, tracker: Tracker):
        self._tracker = tracker
        self._battery = battery
        self._stop = 0
        self._root = tk.Tk()
        self._root.title("Battery Optimizer Interface")
        self._root.geometry("500x500")
        self._labels = Labels(self._root, self._battery)
        self._batteryLevels = []
        self.generatePercentages()
        self._selected = tk.IntVar(self._root, self._batteryLevels[0])
        self._labels.setSelected(self._batteryLevels[0])

        self._modeButton = tk.Button(self._root, text="Modes", font=15, command=lambda: self.modes()).grid(row=1, column=0)
        self._graphButton = tk.Button(self._root, text="Show on Graph", font=15, command=lambda: self.graph()).grid(row=5, column=0)
        self._menu = tk.OptionMenu(self._root, self._selected, *self._batteryLevels, command=lambda x: self.setSelectedThreshold())
        self._menu.configure(font=15)
        self._menu['menu'].configure(font=15)
        self._root.mainloop()

    def setSelectedThreshold(self):
        self._labels.setSelected(self._selected.get())
        self._battery.setUpperThreshold(self._selected.get())

    def generatePercentages(self):
        for i in range (100, -10, -10):
            self._batteryLevels.append(i)

    def modes(self):
        if self._tracker.get_mode() == "Bypass":
            self._tracker.set_auto()
            self._labels.setSelectedMode("Auto")
            self._labels.deleteLabelsForThreshold()
            self._menu.grid_remove()
        else:
            self._tracker.set_bypass()
            self._labels.setSelectedMode("Bypass")
            self._menu.grid(row=3, column=0)
            self._labels.createLabelsForThreshold()
            self._selected.set(self._batteryLevels[0])

    def graph(self):
        g = Graph(self._battery, self._tracker)
        g.show()

    def stop(self):
        self._stop = 1

if __name__ == "__main__":
    b = Battery()
    t = Tracker(b)
    gui = GUI(b, t)
    gui.stop()
    b.stop()
    t.exit()