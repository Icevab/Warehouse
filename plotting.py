import main
import matplotlib.pyplot as plt

def test_plot():
    x = [1, 2, 3]
    y = [2, 4, 1]

    plt.plot(x, y)

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    plt.title("My first graph")

    plt.show()
    
def plot_report(w: main.Warehouse, title):
    pass