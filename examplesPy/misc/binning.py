from dataclasses import dataclass
from itertools import groupby

# snippet: main
if __name__ == '__main__':
    @dataclass
    class Person:
        age: int

    persons = [Person(1), Person(23), Person(18), Person(8)]

    def age_group(person: Person) -> str:
        if person.age <= 12:
            return "Child"
        elif 13 <= person.age <= 20:
            return "Teenager"
        else:
            return "Adult"

    grouped_by_age_group = {}
    for person in persons:
        key = age_group(person)
        group = grouped_by_age_group.get(key, [])
        group.append(person)
        grouped_by_age_group[key] = group
    print(grouped_by_age_group)
# snippet: /main
