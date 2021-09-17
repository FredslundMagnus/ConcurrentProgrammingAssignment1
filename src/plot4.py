import matplotlib.pyplot as plt
from seaborn import heatmap

# data_4 = [
# [0.058130, 0.038628, 0.027961, 0.022111, 0.026308],
# [0.055878, 0.037879, 0.036541, 0.029259, 0.024681],
# [0.056959, 0.047256, 0.024136, 0.026478, 0.024979]
# ] # old

data_4 = [
    [1.35, 2.37, 2.59, 2.76, 2.81],
    [0.88, 1.47, 2.11, 3.20, 1.33],
    [1.47, 2.13, 1.99, 2.63, 3.07]
]


# data_5 = [[0.106361, 0.079162, 0.078486, 0.049976, 0.034296], [0.091244, 0.079936, 0.047931, 0.051310, 0.040113], [0.106956, 0.078486, 0.056372, 0.049171, 0.049484]] # old

data_5 = [
    [0.94, 1.53, 1.81, 2.11, 2.34],
    [0.93, 1.44, 1.43, 2.49, 2.20],
    [0.85, 1.34, 1.99, 2.03, 2.09]
]


def p(data, t):
    heatmap(data, xticklabels=[1, 2, 4, 8, 16], yticklabels=[1000, 100, 10], cmap="Greens")
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
