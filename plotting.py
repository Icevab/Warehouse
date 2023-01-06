import main
import matplotlib.pyplot as plt
from paperwork import take_data_from_txt, Report, commands_of_data

# TODO: Maybe work with .ipynb

def test_plot():
    
    x = [1, 2]
    y = [54.23 + 3.48, 54.23]

    plt.plot(x, y)

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    plt.title("My first graph")

    plt.show()
    
# test_plot()
    
def plot_report():
    print("What do you want a plot of?")
    print("To choose, write first letters of the name of stat,")
    print("For example: write mm to get plot of money made")
    print("Stats available: ")
    data = take_data_from_txt("misc/report_example.txt")
    commands = commands_of_data(data)
    
    for abr, stat in commands.items():
        print(f"{abr} - {stat}")
    
    inp = input()
    
    for key, value in commands.items():
        if key == inp:
            print(data[value])

plot_report()