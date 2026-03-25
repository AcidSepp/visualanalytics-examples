import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = [1500, 2300, 1800, 2700, 3100, 2500]
    df = pd.DataFrame(data)
    df.plot.bar(
        figsize=(8, 5),
        legend=False
    )

    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
