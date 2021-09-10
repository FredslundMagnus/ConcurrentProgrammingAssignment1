import matplotlib.pyplot as plt
from seaborn import heatmap

data_4 = [[0.058130, 0.038628, 0.027961, 0.022111, 0.026308], [0.055878, 0.037879, 0.036541, 0.029259, 0.024681], [0.056959, 0.047256, 0.024136, 0.026478, 0.024979]]

data_5 = [[0.106361, 0.079162, 0.078486, 0.049976, 0.034296], [0.091244, 0.079936, 0.047931, 0.051310, 0.040113], [0.106956, 0.078486, 0.056372, 0.049171, 0.049484]]


def p(data, t):
    heatmap(data, xticklabels=[1, 2, 4, 8, 16], yticklabels=[1000, 100, 10], cmap="Reds")
    # plt.plot(x, y)
    plt.title("Heatmap over speed " + t)
    plt.xlabel("N-Threads")
    plt.ylabel("N-tasks")
    # plt.show()

    # plt.plot(x[:10], y[:10])
    # plt.title("Spedup based on number of tasks " + t)
    # plt.xlabel("N-tasks")
    # plt.ylabel("Times faster")
    plt.show()


p(data_4, "Opg 4")
p(data_5, "Opg 5")
