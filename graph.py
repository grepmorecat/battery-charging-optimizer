import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from battery_simulated import Battery
from tracker import Tracker
import time
import datetime


class Graph:

    def __init__(self, battery: Battery, tracker: Tracker):
        # start collections with zeros
        self.tracker = tracker
        self.battery = battery
        self.history_queue = [0] * 20
        self.time_queue = [0.0] * 20
        # define and adjust figure
        self.fig = plt.figure(figsize=(12, 6), facecolor='#DEDEDE')
        self.ax = plt.subplot(1, 1, 1)
        self.ax.set_facecolor('#DEDEDE')

    def func(self, interval):
        # function to update the data
        info = self.battery.get_info()
        self.history_queue.append(info[0])
        self.history_queue.pop(0)
        self.time_queue.append(time.time())
        self.time_queue.pop(0)
        # clear axis
        self.ax.cla()
        x = [i for i in range(20)]
        labels = [datetime.datetime.fromtimestamp(i).strftime('%M:%S.%f')[:-5] for i in self.time_queue]
        self.ax.plot(self.history_queue)
        self.ax.scatter(len(self.history_queue) - 1, self.history_queue[-1])
        self.ax.text(len(self.history_queue) - 1, self.history_queue[-1] + 2, "{}%".format(self.history_queue[-1]))
        self.ax.set_ylim(0, 100)
        plt.xticks(x, labels)
        plt.setp(self.ax.get_xticklabels(), rotation=30, ha='right')
        # https://pythonguides.com/matplotlib-x-axis-label/#Matplotlib_x-axis_label_overlap

        plt.text(0, 85, "Current State: " + info[1], fontsize=16, color="C2" if info[1] == "Charging" else "C1")
        plt.text(0, 90, "Current Mode: " + self.tracker.get_mode(), fontsize=16,
                 color="C2" if self.tracker.get_mode() == "Auto" else "C1")
        plt.text(0, 80, "Current Level: " + str(info[0]) + "%", fontsize=16)

    def show(self):
        # animate
        global ani
        ani = FuncAnimation(self.fig, self.func, interval=150)
        plt.show()


if __name__ == "__main__":
    b = Battery()
    t = Tracker(b)
    g = Graph(b, t)
    g.show()
    print(111)
    print("exiting")
    t.exit()
