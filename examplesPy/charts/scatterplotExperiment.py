import random
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    mu = 0
    sigma = 0.2

    var = [[random.gauss(mu, sigma), it] for it in range(0, 1000)]
    df = pd.DataFrame(
        var,
        columns=["length", "width"],
    )
    ax1 = df.plot.scatter(x="length", y="width", c="Black")
    ax1.set_ylim(0, 1000)
    ax1.set_xlim(1, -1)
    plt.tight_layout()
    plt.show()
