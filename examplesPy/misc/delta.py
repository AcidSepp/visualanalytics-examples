# snippet: main
def deltas(input: list[float]) -> list[float]:
    output = []
    for i in range(1, len(input)):
        delta = input[i] - input[i - 1]
        output.append(delta)
    return output

if __name__ == '__main__':
    my_list = [1.0, 2.0, 3.0, 18.0]
    print(deltas(my_list))
# snippet: /main
