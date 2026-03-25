# snippet: main
if __name__ == '__main__':
    list1 = [3, 4, 5, 6, 1, 2]
    print(sorted(list1))
    print(sorted(list1, reverse=True))

    list2 = [(3, 4), (4, 2), (4, 10), (7, 1)]
    print(sorted(list2, key=lambda x: x[0]))
    print(sorted(list2, key=lambda x: x[1]))
# snippet: /main
