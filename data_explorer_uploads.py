import json


def load_json(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    return None


numbers = set()

data = load_json("upload_cards2.json")

for card in data:
    if len(card["energyTypes"]) > 0:
        card.update(
            {
                "mainType": card["energyTypes"][0]
            }
        )
    else:
        card.update("mainType": "{Trainer")

# output_file = "upload_cards2.json"
# with open(output_file, "w") as file:
#     json.dump(data, file, indent=4)
