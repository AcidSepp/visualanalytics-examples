import pandas as pd
import matplotlib.pyplot as plt

# snippet: main
if __name__ == '__main__':
    data = [n / 100 for n in range(0,100)]

    df = pd.DataFrame(data)
    df.plot.line(
        figsize=(8, 5),
        legend=False
    )

    plt.xlabel("Anzahl rote Kugeln")
    plt.ylabel("Wahrscheinlichkeit, rote Kugel zu ziehen")

    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
# snippet: /main
