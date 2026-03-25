import json

import requests

# snippet: main
if __name__ == '__main__':
    response = requests.get(
        "https://pokeapi.co/api/v2/pokemon/ditto"
    )

    json_data = response.json()
    pretty_json_string = json.dumps(json_data, indent=2)
    print(pretty_json_string)
# snippet: /main
