from dataclasses import dataclass

import requests

# snippet: requestPokemon
@dataclass
class Pokemon:
    name: str
    weight: int
    height: int


def request_pokemon(name: str) -> Pokemon:
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name}"
    )
    json_data = response.json()

    return Pokemon(
        name=json_data["name"],
        weight=json_data["weight"],
        height=json_data["height"],
    )
# snippet: /requestPokemon

# snippet: main
if __name__ == '__main__':
    treecko = request_pokemon("treecko")
    print(treecko)
    torchic = request_pokemon("torchic")
    print(torchic)
    mudkip = request_pokemon("mudkip")
    print(mudkip)
# snippet: /main

