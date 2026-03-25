# snippet: readCsv
def read_csv(path: str) -> list[list[str]]:
    with open(path) as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.strip().split(","))
    return data
# snippet: /readCsv
