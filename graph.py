import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from battery_simulated import Battery
from tracker import Tracker
import time
import datetime

# TODO add discharging-depth info
# TODO fix high system usage

class Graph:
    """
        This is a graph of the data I plotted using Matplotlib for real-time battery monitoring
        The graph is animated using FuncAnimation, which is a function that takes in a time interval
        The function that is passed in is the update function, which updates the graph every 1000 milliseconds.
        The graph is updated by appending the new data to the list and then plotting the list and clearing it,
        the graph is animated by clearing the graph and then plotting the list again
    """

    def __init__(self, battery: Battery, tracker: Tracker):
        """
        initialize the graph
        :param battery: the battery object
        :param tracker: the tracker object
        """
        # start collections with zeros
        self.tracker = tracker
        self.battery = battery
        # initialize the battery and tracker
        self.history_queue = [0] * 20
        self.time_queue = [0.0] * 20
        # define and adjust figure
        self.fig = plt.figure(figsize=(12, 6), facecolor='#DEDEDE')
        # create a figure with a size of 12 by 6 and a color of #DEDEDE
        self.ax = plt.subplot(1, 1, 1)
        # create a subplot with 1 row and 1 column
        self.ax.set_facecolor('#DEDEDE')
        # create a subplot with a color of #DEDEDE

    def func(self, interval):
        """
        update the graph
        :param interval: the interval of the graph
        :return: the updated graph
        """
        info = self.battery.get_info()
        # the first element in the list and append the new data to the list, clear the axis and plot the list again
        self.history_queue.append(info[0])
        self.history_queue.pop(0)
        self.time_queue.append(time.time())
        self.time_queue.pop(0)
        # clear axis
        self.ax.cla()

        x = [i for i in range(20)]
        # create a list of numbers from 0 to 19
        labels = [datetime.datetime.fromtimestamp(i).strftime('%M:%S.%f')[:-5] for i in self.time_queue]
        # The labels are the time in minutes, seconds, and milliseconds

        # set plot
        self.ax.plot(self.history_queue)
        self.ax.scatter(len(self.history_queue) - 1, self.history_queue[-1])
        self.ax.text(len(self.history_queue) - 1, self.history_queue[-1] + 2, "{}%".format(self.history_queue[-1]))
        self.ax.set_ylim(0, 100)

        # set horizontal line
        threshold = self.tracker.get_range()
        plt.axhline(threshold)
        self.ax.text(0, threshold - 5, "Current Range: " + str(threshold) + "%", fontsize=16)

        # set the y-axis to be from 0 to 100
        plt.xticks(x, labels)
        plt.setp(self.ax.get_xticklabels(), rotation=30, ha='right')
        # rotate the x-axis labels by 30 degrees
        # https://pythonguides.com/matplotlib-x-axis-label/#Matplotlib_x-axis_label_overlap

        # set display info
        plt.text(0, 85, "State: " + info[1], fontsize=16, color="C2" if info[1] == "Charging" else "C1")
        plt.text(0, 90, "Mode: " + self.tracker.get_mode(), fontsize=16,
                 color="C2" if self.tracker.get_mode() == "Auto" else "C1")
        plt.text(0, 80, "Level: " + str(info[0]) + "%", fontsize=16)

        # plt.fill_between(x, self.history_queue, alpha=0.25, color="green")

    def show(self):
        """
        show the graph
        :return:
        """
        global ani
        ani = FuncAnimation(self.fig, self.func, interval=200)
        # animate the graph
        plt.show()


if __name__ == "__main__":
    b = Battery()
    b.set_workload(5)
    t = Tracker(b)
    g = Graph(b, t)

    g.show()
    b.exit()
    t.exit()
    print("exiting")
