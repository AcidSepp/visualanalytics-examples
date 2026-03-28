import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

if __name__ == '__main__':

    mu = 0
    sigma = 0.1
    amount_points = 1000

    var = [[random.gauss(mu, sigma), it] for it in range(0, amount_points)]
    df = pd.DataFrame(
        var,
        columns=["length", "width"],
    )

    fig, ax1 = plt.subplots()

    ax1.scatter(df["length"], df["width"], c="Black", s=5)
    ax1.set_ylim(0, amount_points)
    ax1.set_xlim(-1, 1)
    ax1.set_xlabel("length")
    ax1.set_ylabel("width")

    ax2 = ax1.twinx()
    x_vals = df["length"].values
    kde = gaussian_kde(x_vals)
    x_range = np.linspace(-1, 1, 200)
    density = kde(x_range)
    ax2.plot(x_range, density, c="Red", linewidth=2, label="Gaussian KDE")
    ax2.set_ylabel("density", color="Red")
    ax2.tick_params(axis="y", labelcolor="Red")
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()
