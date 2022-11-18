import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from battery_simulated import Battery
from tracker import Tracker
import time


class Graph:

    def __init__(self, battery: Battery, tracker: Tracker):
        # start collections with zeros
        self.tracker = tracker
        self.battery = battery
        self.history_queue = [0] * 20
        self.time_queue = [0.0] * 20
        # define and adjust figure
        self.fig = plt.figure(figsize=(12, 6), facecolor='#DEDEDE')
        self.ax = plt.subplot(1,1,1)
        self.ax.set_facecolor('#DEDEDE')

    def func(self, interval):
        # function to update the data
        self.history_queue.pop(0)
        self.history_queue.append(self.battery.get_info()[0])
        self.time_queue.pop(0)
        self.time_queue.append(time.time())
        # clear axis
        self.ax.cla()
        # plot cpu
        x = [i for i in range(20)]
        import datetime
        labels = [datetime.datetime.fromtimestamp(i).strftime('%M:%S.%f')[:-5] for i in self.time_queue]
        self.ax.plot(self.history_queue)
        self.ax.scatter(len(self.history_queue) - 1, self.history_queue[-1])
        self.ax.text(len(self.history_queue) - 1, self.history_queue[-1] + 2, "{}%".format(self.history_queue[-1]))
        self.ax.set_ylim(0, 100)
        plt.xticks(x,labels )
        plt.setp(self.ax.get_xticklabels(), rotation=30, ha='right')
        # https://pythonguides.com/matplotlib-x-axis-label/#Matplotlib_x-axis_label_overlap

    def show(self):
        # animate
        global ani
        ani = FuncAnimation(self.fig, self.func, interval=100)
        plt.show()


if __name__ == "__main__":
    b = Battery()
    t = Tracker(b)
    g = Graph(b, t)
    g.show()
    print(111)
    print("exiting")
    t.exit()
