# snippet: distinctCounts
def distinct_counts(collection: list) -> list[tuple]:
    result = {}
    for item in collection:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return list(result.items())
# snippet: /distinctCounts

# snippet: main
if __name__ == '__main__':
    text = "hello world"
    counts = distinct_counts(list(text))
    counts.sort(key=lambda count_tuple: count_tuple[1], reverse=True)
    for char, count in counts:
        print(f"{char}:{count}")
# snippet: /main
