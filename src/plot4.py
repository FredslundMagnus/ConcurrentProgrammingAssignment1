import matplotlib.pyplot as plt
from seaborn import heatmap

# data_4 = [
# [0.058130, 0.038628, 0.027961, 0.022111, 0.026308],
# [0.055878, 0.037879, 0.036541, 0.029259, 0.024681],
# [0.056959, 0.047256, 0.024136, 0.026478, 0.024979]
# ] # old

# data_4 = [
#     [1.35, 2.37, 2.59, 2.76, 2.81],
#     [0.88, 1.47, 2.11, 3.20, 1.33],
#     [1.47, 2.13, 1.99, 2.63, 3.07]
# ]

data_4 = [
    [1.09, 2.16, 4.06, 6.30, 5.98],
    [1.06, 2.11, 4.15, 5.79, 5.70],
    [1.01, 1.99, 3.28, 4.34, 4.87]
]


# threads-1-tasks-10.txt: Average speedup:    1.01
# threads-1-tasks-100.txt: Average speedup:   1.06
# threads-1-tasks-1000.txt: Average speedup:  1.09
# threads-2-tasks-10.txt: Average speedup:    1.99
# threads-2-tasks-100.txt: Average speedup:   2.11
# threads-2-tasks-1000.txt: Average speedup:  2.16
# threads-4-tasks-10.txt: Average speedup:    3.28
# threads-4-tasks-100.txt: Average speedup:   4.15
# threads-4-tasks-1000.txt: Average speedup:  4.06
# threads-8-tasks-10.txt: Average speedup:    4.34
# threads-8-tasks-100.txt: Average speedup:   5.79
# threads-8-tasks-1000.txt: Average speedup:  6.30
# threads-16-tasks-10.txt: Average speedup:   4.87
# threads-16-tasks-100.txt: Average speedup:  5.70
# threads-16-tasks-1000.txt: Average speedup: 5.98

# data_5 = [[0.106361, 0.079162, 0.078486, 0.049976, 0.034296], [0.091244, 0.079936, 0.047931, 0.051310, 0.040113], [0.106956, 0.078486, 0.056372, 0.049171, 0.049484]] # old

# data_5 = [
#     [0.94, 1.53, 1.81, 2.11, 2.34],
#     [0.93, 1.44, 1.43, 2.49, 2.20],
#     [0.85, 1.34, 1.99, 2.03, 2.09]
# ]


data_5 = [
    [0.950, 2.810, 5.600, 10.19, 11.51],
    [1.090, 2.630, 5.820, 10.59, 18.58],
    [0.930, 2.480, 5.190, 6.390, 11.20]
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
