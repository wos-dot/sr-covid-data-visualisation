import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import functools as ft

ages = []
ignorefirst = True
with open("./covid19-data/Deaths/OpenData_Slovakia_Covid_Deaths_AgeGroup_District.csv", encoding="latin1") as f:
    for line in f.readlines():
        if ignorefirst:
            ignorefirst = False
            continue
        cells = list(map(lambda x: x.strip(), line.split(";")))
        ages.append(int(cells[3]))
    #print(ages)
    fig, axs = plt.subplots(1, 1, sharey=True, tight_layout=True, figsize=(15,10))
    freq, bins, patches = axs.hist(x=ages, bins=list(set(ages)))

    # x coordinate for labels
    bin_centers = np.diff(bins)*0.5 + bins[:-1]

    n = 0
    for fr, x, patch in zip(freq, bin_centers, patches):
        height = int(freq[n])
        plt.annotate("{}".format(height),
                     # top left corner of the histogram bar
                     xy=(x, height),
                     # offsetting label position above its bar
                     xytext=(0, 0.2),
                     # Offset (in points) from the *xy* value
                     textcoords="offset points",
                     ha='center', va='bottom'
                     )
        n = n+1
    axs.grid()
    axs.set_xlabel("Vek[počet rokov]")
    axs.set_xticks(list(set(ages)))
    axs.set_ylabel("Počet úmrtí")
    plt.savefig("sr-covid-deaths-age-group.png",
                format="png", bbox_inches="tight")
    plt.show()
