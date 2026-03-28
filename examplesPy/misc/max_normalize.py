# snippet: main
def max_normalize(input: list[float]) -> list[float]:
    max_val = max(input)
    return [x / max_val for x in input]
# snippet: /main
