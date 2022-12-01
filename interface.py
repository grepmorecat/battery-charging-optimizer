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
    users can also see an image of their battery and its capacity
    '''
    def __init__(self, battery: Battery, tracker: Tracker):
        '''
        self._tracker - tracker class
        self._battery - battery class
        self._root - root window of tkinter
        self._batteryImage - calls the battery_image class
        self._labels - calls the labels class
        self._batteryLevels - list holds battery levels in increments of 10 from 0 to 100
        self._selected - variable that holds which battery level is selected in the option menu
        self._modeButton - button to swap modes
        self._graphButton - button to show the graph with info on the battery
        self._menu - a dropdown option menu with battery levels to allow user to select their preferred threshold in bypass mode
        '''
        self._tracker = tracker
        self._battery = battery
        self._stop = 0

        self._root = tk.Tk()
        self._root.title("Battery Optimizer Interface") #set the title of the window
        self._root.geometry("350x225") #set size of the window

        self._batteryLevels = []
        self.generatePercentages()  # calls a method to generate numbers for self._batteryLevels

        self._batteryImage = Battery_Image(self._root)
        self._labels = Labels(self._root, self._battery, self._batteryImage)

        self._selected = tk.IntVar(self._root, self._batteryLevels[0]) #set the starting max threshold to 100
        self._labels.setSelected(self._batteryLevels[0]) #set the label

        self._modeButton = tk.Button(self._root, text="Modes", font=15, command=lambda: self.modes()).grid(row=1, column=0, padx=10, pady=5)
        self._graphButton = tk.Button(self._root, text="Show on Graph", font=15, command=lambda: self.graph()).grid(row=5, column=0, padx=15, pady=5)

        self._menu = tk.OptionMenu(self._root, self._selected, *self._batteryLevels, command=lambda x: self.setSelectedThreshold())
        self._menu.configure(font=15, padx=10, pady=5)
        self._menu['menu'].configure(font=15) #set fontsize of menu options

        self._root.mainloop()

    def setSelectedThreshold(self):
        '''
        method is called when an option menu is selected
        sets the selected option as a label and as the max/upper threshold
        '''
        self._labels.setSelected(self._selected.get())
        self._battery.setUpperThreshold(self._selected.get())

    def generatePercentages(self):
        '''method is used to generate all percentages in increments of 10 in reverse order'''
        for i in range (100, -10, -10):
            self._batteryLevels.append(i)

    def modes(self):
        '''method is called when mode button is pressed'''
        if self._tracker.get_mode() == "Bypass":
            '''
            if mode is in bypass
            swap mode to auto mode
            delete the label or max threshold
            delete the option menu (so users can use it if in auto mode)
            set window size back to original
            reset the image of the battery back to original position
            '''
            self._tracker.set_auto()
            self._labels.setSelectedMode("Auto")
            self._labels.deleteLabelsForThreshold()
            self._menu.grid_remove()
            self._root.geometry("350x225")
            self._batteryImage.interfaceAutoGrid()
        else:
            '''
            if mode is in auto
            set mode to bypass
            show the menu option for thresholds
            create the labels to show thresholds selected
            set the starting max threshold 100(which is first item in the list)
            enlarge the window size for better view
            set the image of the battery 
            '''
            self._tracker.set_bypass()
            self._labels.setSelectedMode("Bypass")
            self._menu.grid(row=3, column=0)
            self._labels.createLabelsForThreshold()
            self._selected.set(self._batteryLevels[0])
            self._root.geometry("400x300")
            self._batteryImage.interfaceBypassGrid()

    def graph(self):
        '''method is called when the graph button is pressed'''
        g = Graph(self._battery, self._tracker)
        g.show()


if __name__ == "__main__":
    b = Battery()
    t = Tracker(b)
    gui = GUI(b, t)
    gui.stop()
    b.stop()
    t.exit()