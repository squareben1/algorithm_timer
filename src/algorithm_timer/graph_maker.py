import matplotlib.pyplot as plt
import numpy as np


def create_graph(time_results, arr_length, func_name):
    # plot the axes
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    x = np.array(arr_length)
    y = np.array(time_results)
    plt.plot(x, y, c='red', alpha=0.5)
    # Format plot
    plt.title(f"{func_name}", fontsize=24)
    plt.xlabel('Arr length', fontsize=16)
    plt.ylabel("Time taken", fontsize=16)
    ax.set_ylim(ymin=0)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
