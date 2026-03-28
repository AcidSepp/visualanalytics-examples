# snippet: readCsv
def read_csv(path):
    with open(path) as f:
        lines = f.readlines()
        data = []
        for line in lines:
            splits = line.strip().split(",")
            heads = True if splits[1] == "1" else False
            data.append((splits[0], heads))
        return data
# snippet: /readCsv

# snippet: groupByName
def group_by_name(data: list) -> dict[str, list]:
    grouped = {}
    for datum in data:
        key = datum[0]
        group = grouped.get(key, [])
        group.append(datum)
        grouped[key] = group
    return grouped
# snippet: /groupByName


if __name__ == '__main__':
    data = read_csv("coinChartRawData.csv")
    print(data)

# snippet: filter
    filtered = list(filter(lambda it: it[1], data))
    print(filtered)
# snippet: /filter

    grouped = group_by_name(filtered)
    print(grouped)

# snippet: count
    mapped = dict(map(lambda kv: (kv[0], len(kv[1])), grouped.items()))
    print(mapped)
# snippet: /count

# snippet: ppf
    from scipy import stats
    print(stats.binom(n=100, p=0.5).ppf(0.9999))
# snippet: /ppf

