import matplotlib.pyplot as plt

def create_graph(time_results, arr_length):
    # plot the axes
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    plt.plot(arr_length, time_results, c='red', alpha=0.5)
    # Format plot.
    plt.title("Algo Timing", fontsize=24)
    plt.xlabel('Arr length', fontsize=16)
    plt.ylabel("Time taken", fontsize=16)
    ax.set_ylim(ymin=0)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()