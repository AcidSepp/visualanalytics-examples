# snippet: main
import numpy as np

def print_statistics(input: list[float]):
    data = np.array(input)
    print(np.percentile(data, 25))
    print(np.percentile(data, 75))
    print(np.percentile(data, 50))
    print(np.std(data))
# snippet: /main
