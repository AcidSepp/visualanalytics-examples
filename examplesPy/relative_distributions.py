# snippet: main
def relative_distributions(collection: list) -> dict:
    result = {}
    for item in collection:
        result[item] = result.get(item, 0) + 1
    return result


if __name__ == '__main__':
    my_list = [1, 3, 3, 7]
    print(relative_distributions(my_list))
# snippet: /main
