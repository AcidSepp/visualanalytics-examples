# snippet: main
def naive_moving_average(input: list[float]) -> list[float]:
    current_sum = 0.0
    result = []
    for index, value in enumerate(input):
        current_sum += value
        result.append(current_sum / (index + 1))
    return result
# snippet: /main
