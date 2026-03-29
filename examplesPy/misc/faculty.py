import pandas as pd
import matplotlib.pyplot as plt

def faculty(n: int) -> int:
    result: int = 1
    while n > 0:
        result = result * n
        n = n - 1
    return result

# snippet: main
if __name__ == '__main__':
    data = [faculty(n) for n in range(0,5)]

    df = pd.DataFrame(data)
    df.plot.bar(
        figsize=(8, 5),
        legend=False
    )

    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
# snippet: /main
