import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import collections

from battery import Battery


# function to update the data
def graph_setup(interval):
    history_queue.popleft()
    history_queue.append(battery.get_info()[0])
    # clear axis
    ax.cla()
    # plot cpu
    # todo: fill with time stamps
    # x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    x = [i for i in range(20)]
    ax.plot(history_queue)
    ax.scatter(len(history_queue) - 1, history_queue[-1])
    ax.text(len(history_queue) - 1, history_queue[-1] + 2, "{}%".format(history_queue[-1]))
    ax.set_ylim(0, 100)
    plt.xticks(x)


# start collections with zeros
battery = Battery()
history_queue = collections.deque([0] * 20, maxlen=20)
# define and adjust figure
fig = plt.figure(figsize=(12, 6), facecolor='#DEDEDE')
ax = plt.subplot(111)
ax.set_facecolor('#DEDEDE')
# animate
ani = FuncAnimation(fig, graph_setup, interval=500)
plt.show()
