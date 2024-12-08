import json


def edit_json_file(input_file, output_file):
    # Load the JSON file
    with open(input_file, "r") as file:
        data = json.load(file)

    # Edit the data
    for card in data:
        if len(card["energyTypes"]) > 0:
            card.update({"mainType": card["energyTypes"][0]})
    else:
        card.update({"mainType": "~Trainer"})

    # Save the updated JSON to a new file
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)


# Example usage
input_file = "updated_cards.json"  # Input JSON file
output_file = "updated_cards2.json"  # Output JSON file
edit_json_file(input_file, output_file)
