import tkinter as tk

class Labels(object):
    '''Labels class holds the labels for the interface'''
    def __init__(self, root, battery, battery_image):
        '''
        self._root - root window of tkinter
        self._battery - battery class
        self._batteryImage - battery image class
        self._selectedMode - the mode selected by the user
        self._selected - max threshold select by the user in bypass mode (default is 100)
        self._level - current battery level
        '''
        self._root = root
        self._battery = battery
        self._batteryImage = battery_image
        self._selectedMode = tk.StringVar()
        self._selected = tk.IntVar()
        self._level = tk.StringVar()

        self._selectedMode.set("Auto") #set the starting selected mode to auto

        tk.Label(self._root, text="Battery Level: ", font=15).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self._root, text="Current Mode:", font=15).grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self._root, textvariable=self._selectedMode, font=15).grid(row=2, column=1, pady=5)

        self._thresholdLabel = tk.Label(self._root, text="Setting Threshold to: ", font=15)
        self._thresholdLevelLabel = tk.Label(self._root, textvariable=self._selected, font=15)

        self._level.set(self._battery.getLevel()) #get the current battery level and set it to variable
        self._labelBattery = tk.Label(self._root, textvariable=self._level, font=15)
        self._labelBattery.grid(row=0, column=1)

        self.loadBatteryLevel() #call the function loadBatteryLevel to consistently get new battery readings

    def loadBatteryLevel(self):
        '''
        method will consistantly read the battery levels and set it to the variable self._level
        a new label is set with the new battery readings
        set the battery image to the new battery level
        call the loadBatteryLevel function again after 1second
        '''
        self._level.set(self._battery.getLevel())
        self._labelBattery.config(textvariable=self._level)
        self._batteryImage.setCells(self._battery.getLevel())
        self._labelBattery.after(1000, self.loadBatteryLevel)

    def createLabelsForThreshold(self):
        '''method creates labels for thresholds on the tkinter window'''
        self._thresholdLabel.grid(row=4, column=0, padx=10, pady=10)
        self._thresholdLevelLabel.grid(row=4, column=1, padx=10, pady=10)
        self.setSelected(100)

    def deleteLabelsForThreshold(self):
        '''method deleted the threshold labels on the tkinter window'''
        self._thresholdLabel.grid_remove()
        self._thresholdLevelLabel.grid_remove()


    '''getters and setters'''
    #selected
    def getSelected(self):
        return self._selected
    def setSelected(self, selected):
        self._selected.set(selected)

    #selectedMode
    def getSelectedMode(self):
        return self._selectedMode
    def setSelectedMode(self, mode):
        self._selectedMode.set(mode)