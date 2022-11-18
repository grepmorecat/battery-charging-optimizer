import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from battery_simulated import Battery
from tracker import Tracker
import time

"""
    This is a graph of the data I plotted using Matplotlib for real-time battery monitoring
    The graph is animated using FuncAnimation, which is a function that takes in a time interval
    The function that is passed in is the update function, which updates the graph every 1000 milliseconds.
    The graph is updated by appending the new data to the list and then plotting the list and clearing it,
    the graph is animated by clearing the graph and then plotting the list again
"""


class Graph:

    def __init__(self, battery: Battery, tracker: Tracker):
        """
        initialize the graph
        :param battery: the battery object
        :param tracker: the tracker object
        """
        # start collections with zeros
        self.tracker = tracker
        self.battery = battery
        """
        initialize the battery and tracker
        """
        self.history_queue = [0] * 20
        self.time_queue = [0.0] * 20
        # define and adjust figure
        self.fig = plt.figure(figsize=(12, 6), facecolor='#DEDEDE')
        """
        create a figure with a size of 12 by 6 and a color of #DEDEDE
        """
        self.ax = plt.subplot(1, 1, 1)
        """
        
        create a subplot with 1 row and 1 column"""
        self.ax.set_facecolor('#DEDEDE')
        """
        create a subplot with a color of #DEDED
        E"""

    def func(self, interval):
        """
        update the graph
        :param interval: the interval of the graph
        :return: the updated graph
        """
        # function to update the data
        self.history_queue.pop(0)
        self.history_queue.append(self.battery.get_info()[0])
        self.time_queue.pop(0)
        self.time_queue.append(time.time())
        # clear axis
        self.ax.cla()
        """
        pop the first element in the list and append the new data to the list
        clear the axis and plot the list again
        """

        # plot cpu
        x = [i for i in range(20)]
        """
        create a list of numbers from 0 to 19
        """
        import datetime
        labels = [datetime.datetime.fromtimestamp(i).strftime('%M:%S.%f')[:-5] for i in self.time_queue]
        """
        The labels are the time in minutes, seconds, and milliseconds
        """
        self.ax.plot(self.history_queue)
        self.ax.scatter(len(self.history_queue) - 1, self.history_queue[-1])
        self.ax.text(len(self.history_queue) - 1, self.history_queue[-1] + 2, "{}%".format(self.history_queue[-1]))
        self.ax.set_ylim(0, 100)
        """
        set the y-axis to be from 0 to 100
        """
        plt.xticks(x, labels)
        plt.setp(self.ax.get_xticklabels(), rotation=30, ha='right')
        """
        rotate the x-axis labels by 30 degrees
        """
        # https://pythonguides.com/matplotlib-x-axis-label/#Matplotlib_x-axis_label_overlap

    def show(self):
        """
        show the graph
        :return:
        """
        # animate
        global ani
        ani = FuncAnimation(self.fig, self.func, interval=100)
        """
        animate the graph
        """
        plt.show()


if __name__ == "__main__":
    b = Battery()
    t = Tracker(b)
    g = Graph(b, t)
    g.show()
    print(111)
    print("exiting")
    t.exit()
