# snippet: main
def min_max_normalize(input: list[float]) -> list[float]:
    max_val = max(input)
    min_val = min(input)
    return [(x - min_val) / (max_val - min_val) for x in input]
# snippet: /main
