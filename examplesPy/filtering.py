from dataclasses import dataclass

# snippet: main
if __name__ == '__main__':
    @dataclass
    class Person:
        age: int

    persons = [Person(1), Person(23), Person(18), Person(8)]

    only_adults = filter(lambda p: p.age >= 18, persons)

    print(list(only_adults))
# snippet: /main
