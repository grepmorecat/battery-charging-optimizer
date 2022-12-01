import tkinter as tk
from labels import Labels
from graph import Graph
from battery_simulated import Battery
from tracker import Tracker
from battery_image import Battery_Image

class GUI(object):
    '''
    GUI class creates a graphical interface for the user
    it provides the current battery level(percentage)
    users can swap modes using a button
    users can press a button to show what is happening to the battery on a graph
    '''
    def __init__(self, battery: Battery, tracker: Tracker):
        '''
        self._tracker
        self._battery
        self._stop
        self._root
        self._labels
        self._battery_levels
        self._selected
        '''
        self._tracker = tracker
        self._battery = battery
        self._stop = 0
        self._root = tk.Tk()
        self._root.title("Battery Optimizer Interface")
        self._root.geometry("350x225")
        self._battery_image = Battery_Image(self._root)
        self._labels = Labels(self._root, self._battery, self._battery_image)
        self._battery_levels = []
        self.generate_percentages() #calls a method to generate numbers for self._battery_levels
        self._selected = tk.IntVar(self._root, self._battery_levels[0])
        self._labels.setSelected(self._battery_levels[0])

        self._mode_button = tk.Button(self._root, text="Modes", font=15, command=lambda: self.modes()).grid(row=1, column=0, padx=10, pady=5)
        self._graph_button = tk.Button(self._root, text="Show on Graph", font=15, command=lambda: self.graph()).grid(row=5, column=0, padx=15, pady=5)

        self._menu = tk.OptionMenu(self._root, self._selected, *self._battery_levels, command=lambda x: self.setSelectedThreshold())
        self._menu.configure(font=15, padx=10, pady=5)
        self._menu['menu'].configure(font=15)
        self._root.mainloop()

    def setSelectedThreshold(self):
        self._labels.setSelected(self._selected.get())
        self._battery.setUpperThreshold(self._selected.get())

    def generate_percentages(self):
        for i in range (100, -10, -10):
            self._battery_levels.append(i)

    def modes(self):
        if self._tracker.get_mode() == "Bypass":
            self._tracker.set_auto()
            self._labels.setSelectedMode("Auto")
            self._labels.deleteLabelsForThreshold()
            self._menu.grid_remove()
            self._root.geometry("350x225")
            self._battery_image.interfaceAutoGrid()
        else:
            self._tracker.set_bypass()
            self._labels.setSelectedMode("Bypass")
            self._menu.grid(row=3, column=0)
            self._labels.createLabelsForThreshold()
            self._selected.set(self._battery_levels[0])
            self._root.geometry("400x300")
            self._battery_image.interfaceBypassGrid()

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