import matplotlib.pyplot as plt

x = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 300, 400, 1000, 10000]
# y_3 = [1.67, 2.83, 2.75, 2.11, 2.49, 1.78, 2.72, 2.29, 2.13, 3.25, 2.22, 1.95, 2.62, 2.01] # old
# y_5 = [2.11, 2.17, 2.34, 2.35, 2.42, 1.59, 1.87, 1.99, 2.00, 1.87, 1.92, 1.87, 2.11, 1.95]  # old
y_3 = [1.56, 1.50, 2.41, 2.54, 2.91, 2.72, 3.28, 2.54, 3.48, 1.59, 2.88, 2.42, 3.43, 1.89]
y_5 = [1.48, 1.95, 2.71, 2.92, 2.24, 2.55, 2.13, 2.15, 2.39, 2.10, 2.47, 2.09, 2.60, 2.60]


def p(y, t):
    plt.plot(x, y)
    plt.title("Spedup based on number of tasks " + t)
    plt.xlabel("N-tasks")
    plt.ylabel("Times faster")
    plt.show()

    plt.plot(x[:10], y[:10])
    plt.title("Spedup based on number of tasks " + t)
    plt.xlabel("N-tasks")
    plt.ylabel("Times faster")
    plt.show()


p(y_3, "Opg 3")
p(y_5, "Opg 5")
