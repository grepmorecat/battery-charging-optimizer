import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import collections

from battery import Battery


class Graph():

    def __init__(self, battery: Battery):
        # start collections with zeros
        self.battery = battery
        self.history_queue = collections.deque([0] * 20, maxlen=20)
        # define and adjust figure
        self.fig = plt.figure(figsize=(12, 6), facecolor='#DEDEDE')
        self.ax = plt.subplot(111)
        self.ax.set_facecolor('#DEDEDE')

    def func(self, interval):
        # function to update the data
        self.history_queue.popleft()
        self.history_queue.append(self.battery.get_info()[0])
        # clear axis
        self.ax.cla()
        # plot cpu
        # todo: fill with time stamps
        # x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        x = [i for i in range(20)]
        self.ax.plot(self.history_queue)
        self.ax.scatter(len(self.history_queue) - 1, self.history_queue[-1])
        self.ax.text(len(self.history_queue) - 1, self.history_queue[-1] + 2, "{}%".format(self.history_queue[-1]))
        self.ax.set_ylim(0, 100)
        plt.xticks(x)

    def show(self):
        # animate
        global ani
        ani = FuncAnimation(self.fig, self.func, interval=500)
        plt.show()


if __name__ == "__main__":
    g = Graph(Battery())
    g.show()
