import random
import matplotlib.pyplot as plt
import numpy as np


def autolabel(rects):
    # Attach a text label above each bar in *rects*, displaying its height.
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def is_worth(price, throws, step):
    win, costs, labels, earn = [], [], [], []
    cost = 0

    for x in range(0, 5):
        for i in range(0, throws):
            cost += price
            win.append(random.randrange(1, 7))

        labels.append(str(round(price, 2)))
        price += step
        costs.append(round(cost))
        earn.append(sum(win))

        cost = 0
        win.clear()

    return costs, earn, labels


cost, win, labels = is_worth(3.30, 1000, 0.10)

print(cost)
print(win)
print(labels)

# Visualization results.

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, cost, width, label='Cost')
rects2 = ax.bar(x + width / 2, win, width, label='Win')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Money')
ax.set_title('Results after 1000 throws')
ax.set_xlabel('Cost per one throw')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
