import random
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    var = [[random.random(), random.random()] for _ in range(0, 100)]
    df = pd.DataFrame(
        var,
        columns=["length", "width"],
    )
    ax1 = df.plot.scatter(x="length", y="width", c="Black")
    plt.tight_layout()
    plt.show()
