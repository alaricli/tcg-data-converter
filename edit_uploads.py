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


def map_evolution(cardDexNumber):
    evolution_map = {
        "1": {"evolvesFrom": None, "evolvesTo": 2},  # Bulbasaur -> Ivysaur
        "2": {"evolvesFrom": 1, "evolvesTo": 3},  # Ivysaur -> Venusaur
        "3": {"evolvesFrom": 2, "evolvesTo": None},  # Venusaur (final stage)
        "4": {"evolvesFrom": None, "evolvesTo": 5},  # Charmander -> Charmeleon
        "5": {"evolvesFrom": 4, "evolvesTo": 6},  # Charmeleon -> Charizard
        "6": {"evolvesFrom": 5, "evolvesTo": None},  # Charizard (final stage)
        "7": {"evolvesFrom": None, "evolvesTo": 8},  # Squirtle -> Wartortle
        "8": {"evolvesFrom": 7, "evolvesTo": 9},  # Wartortle -> Blastoise
        "9": {"evolvesFrom": 8, "evolvesTo": None},  # Blastoise (final stage)
        "10": {"evolvesFrom": None, "evolvesTo": 11},  # Caterpie -> Metapod
        "11": {"evolvesFrom": 10, "evolvesTo": 12},  # Metapod -> Butterfree
        "12": {"evolvesFrom": 11, "evolvesTo": None},  # Butterfree (final stage)
        "13": {"evolvesFrom": None, "evolvesTo": 14},  # Weedle -> Kakuna
        "14": {"evolvesFrom": 13, "evolvesTo": 15},  # Kakuna -> Beedrill
        "15": {"evolvesFrom": 14, "evolvesTo": None},  # Beedrill (final stage)
        "16": {"evolvesFrom": None, "evolvesTo": 17},  # Pidgey -> Pidgeotto
        "17": {"evolvesFrom": 16, "evolvesTo": 18},  # Pidgeotto -> Pidgeot
        "18": {"evolvesFrom": 17, "evolvesTo": None},  # Pidgeot (final stage)
        "19": {"evolvesFrom": None, "evolvesTo": 20},  # Rattata -> Raticate
        "20": {"evolvesFrom": 19, "evolvesTo": None},  # Raticate (final stage)
        "21": {"evolvesFrom": None, "evolvesTo": 22},  # Spearow -> Fearow
        "22": {"evolvesFrom": 21, "evolvesTo": None},  # Fearow (final stage)
        "23": {"evolvesFrom": None, "evolvesTo": 24},  # Ekans -> Arbok
        "24": {"evolvesFrom": 23, "evolvesTo": None},  # Arbok (final stage)
        "25": {"evolvesFrom": None, "evolvesTo": 26},  # Pikachu -> Raichu
        "26": {"evolvesFrom": 25, "evolvesTo": None},  # Raichu (final stage)
        "27": {"evolvesFrom": None, "evolvesTo": 28},  # Sandshrew -> Sandslash
        "28": {"evolvesFrom": 27, "evolvesTo": None},  # Sandslash (final stage)
        "29": {"evolvesFrom": None, "evolvesTo": 30},  # Nidoran♀ -> Nidorina
        "30": {"evolvesFrom": 29, "evolvesTo": 31},  # Nidorina -> Nidoqueen
        "31": {"evolvesFrom": 30, "evolvesTo": None},  # Nidoqueen (final stage)
        "32": {"evolvesFrom": None, "evolvesTo": 33},  # Nidoran♂ -> Nidorino
        "33": {"evolvesFrom": 32, "evolvesTo": 34},  # Nidorino -> Nidoking
        "34": {"evolvesFrom": 33, "evolvesTo": None},  # Nidoking (final stage)
        "35": {"evolvesFrom": None, "evolvesTo": 36},  # Clefairy -> Clefable
        "36": {"evolvesFrom": 35, "evolvesTo": None},  # Clefable (final stage)
        "37": {"evolvesFrom": None, "evolvesTo": 38},  # Vulpix -> Ninetales
        "38": {"evolvesFrom": 37, "evolvesTo": None},  # Ninetales (final stage)
        "39": {"evolvesFrom": None, "evolvesTo": 40},  # Jigglypuff -> Wigglytuff
        "40": {"evolvesFrom": 39, "evolvesTo": None},  # Wigglytuff (final stage)
        "41": {"evolvesFrom": None, "evolvesTo": 42},  # Zubat -> Golbat
        "42": {"evolvesFrom": 41, "evolvesTo": None},  # Golbat (final stage)
        "43": {"evolvesFrom": None, "evolvesTo": 44},  # Oddish -> Gloom
        "44": {"evolvesFrom": 43, "evolvesTo": 45},  # Gloom -> Vileplume
        "45": {"evolvesFrom": 44, "evolvesTo": None},  # Vileplume (final stage)
        "46": {"evolvesFrom": None, "evolvesTo": 47},  # Paras -> Parasect
        "47": {"evolvesFrom": 46, "evolvesTo": None},  # Parasect (final stage)
        "48": {"evolvesFrom": None, "evolvesTo": 49},  # Venonat -> Venomoth
        "49": {"evolvesFrom": 48, "evolvesTo": None},  # Venomoth (final stage)
        "50": {"evolvesFrom": None, "evolvesTo": 51},  # Diglett -> Dugtrio
        "51": {"evolvesFrom": 50, "evolvesTo": None},  # Dugtrio (final stage)
        "52": {"evolvesFrom": None, "evolvesTo": 53},  # Meowth -> Persian
        "53": {"evolvesFrom": 52, "evolvesTo": None},  # Persian (final stage)
        "54": {"evolvesFrom": None, "evolvesTo": 55},  # Psyduck -> Golduck
        "55": {"evolvesFrom": 54, "evolvesTo": None},  # Golduck (final stage)
        "56": {"evolvesFrom": None, "evolvesTo": 57},  # Mankey -> Primeape
        "57": {"evolvesFrom": 56, "evolvesTo": None},  # Primeape (final stage)
        "58": {"evolvesFrom": None, "evolvesTo": 59},  # Growlithe -> Arcanine
        "59": {"evolvesFrom": 58, "evolvesTo": None},  # Arcanine (final stage)
        "60": {"evolvesFrom": None, "evolvesTo": 61},  # Poliwag -> Poliwhirl
        "61": {"evolvesFrom": 60, "evolvesTo": 62},  # Poliwhirl -> Poliwrath
        "62": {"evolvesFrom": 61, "evolvesTo": None},  # Poliwrath (final stage)
        "63": {"evolvesFrom": None, "evolvesTo": 64},  # Abra -> Kadabra
        "64": {"evolvesFrom": 63, "evolvesTo": 65},  # Kadabra -> Alakazam
        "65": {"evolvesFrom": 64, "evolvesTo": None},  # Alakazam (final stage)
        "66": {"evolvesFrom": None, "evolvesTo": 67},  # Machop -> Machoke
        "67": {"evolvesFrom": 66, "evolvesTo": 68},  # Machoke -> Machamp
        "68": {"evolvesFrom": 67, "evolvesTo": None},  # Machamp (final stage)
        "69": {"evolvesFrom": None, "evolvesTo": 70},  # Bellsprout -> Weepinbell
        "70": {"evolvesFrom": 69, "evolvesTo": 71},  # Weepinbell -> Victreebel
        "71": {"evolvesFrom": 70, "evolvesTo": None},  # Victreebel (final stage)
        "72": {"evolvesFrom": None, "evolvesTo": 73},  # Tentacool -> Tentacruel
        "73": {"evolvesFrom": 72, "evolvesTo": None},  # Tentacruel (final stage)
        "74": {"evolvesFrom": None, "evolvesTo": 75},  # Geodude -> Graveler
        "75": {"evolvesFrom": 74, "evolvesTo": 76},  # Graveler -> Golem
        "76": {"evolvesFrom": 75, "evolvesTo": None},  # Golem (final stage)
        "77": {"evolvesFrom": None, "evolvesTo": 78},  # Ponyta -> Rapidash
        "78": {"evolvesFrom": 77, "evolvesTo": None},  # Rapidash (final stage)
        "79": {"evolvesFrom": None, "evolvesTo": 80},  # Slowpoke -> Slowbro
        "80": {"evolvesFrom": 79, "evolvesTo": None},  # Slowbro (final stage)
        "81": {"evolvesFrom": None, "evolvesTo": 82},  # Magnemite -> Magneton
        "82": {"evolvesFrom": 81, "evolvesTo": None},  # Magneton (final stage)
        "83": {"evolvesFrom": None, "evolvesTo": None},  # Farfetch'd (no evolution)
        "84": {"evolvesFrom": None, "evolvesTo": 85},  # Doduo -> Dodrio
        "85": {"evolvesFrom": 84, "evolvesTo": None},  # Dodrio (final stage)
        "86": {"evolvesFrom": None, "evolvesTo": 87},  # Seel -> Dewgong
        "87": {"evolvesFrom": 86, "evolvesTo": None},  # Dewgong (final stage)
        "88": {"evolvesFrom": None, "evolvesTo": 89},  # Grimer -> Muk
        "89": {"evolvesFrom": 88, "evolvesTo": None},  # Muk (final stage)
        "90": {"evolvesFrom": None, "evolvesTo": 91},  # Shellder -> Cloyster
        "91": {"evolvesFrom": 90, "evolvesTo": None},  # Cloyster (final stage)
        "92": {"evolvesFrom": None, "evolvesTo": 93},  # Gastly -> Haunter
        "93": {"evolvesFrom": 92, "evolvesTo": 94},  # Haunter -> Gengar
        "94": {"evolvesFrom": 93, "evolvesTo": None},  # Gengar (final stage)
        "95": {"evolvesFrom": None, "evolvesTo": None},  # Onix (no evolution)
        "96": {"evolvesFrom": None, "evolvesTo": 97},  # Drowzee -> Hypno
        "97": {"evolvesFrom": 96, "evolvesTo": None},  # Hypno (final stage)
        "98": {"evolvesFrom": None, "evolvesTo": 99},  # Krabby -> Kingler
        "99": {"evolvesFrom": 98, "evolvesTo": None},  # Kingler (final stage)
        "100": {"evolvesFrom": None, "evolvesTo": 101},  # Voltorb -> Electrode
        "101": {"evolvesFrom": 100, "evolvesTo": None},  # Electrode (final stage)
        "102": {"evolvesFrom": None, "evolvesTo": 103},  # Exeggcute -> Exeggutor
        "103": {"evolvesFrom": 102, "evolvesTo": None},  # Exeggutor (final stage)
        "104": {"evolvesFrom": None, "evolvesTo": 105},  # Cubone -> Marowak
        "105": {"evolvesFrom": 104, "evolvesTo": None},  # Marowak (final stage)
        "106": {"evolvesFrom": None, "evolvesTo": None},  # Hitmonlee (no evolution)
        "107": {"evolvesFrom": None, "evolvesTo": None},  # Hitmonchan (no evolution)
        "108": {"evolvesFrom": None, "evolvesTo": None},  # Lickitung (no evolution)
        "109": {"evolvesFrom": None, "evolvesTo": 110},  # Koffing -> Weezing
        "110": {"evolvesFrom": 109, "evolvesTo": None},  # Weezing (final stage)
        "111": {"evolvesFrom": None, "evolvesTo": 112},  # Rhyhorn -> Rhydon
        "112": {"evolvesFrom": 111, "evolvesTo": None},  # Rhydon (final stage)
        "113": {"evolvesFrom": None, "evolvesTo": None},  # Chansey (no evolution)
        "114": {"evolvesFrom": None, "evolvesTo": None},  # Tangela (no evolution)
        "115": {"evolvesFrom": None, "evolvesTo": None},  # Kangaskhan (no evolution)
        "116": {"evolvesFrom": None, "evolvesTo": 117},  # Horsea -> Seadra
        "117": {"evolvesFrom": 116, "evolvesTo": None},  # Seadra (final stage)
        "118": {"evolvesFrom": None, "evolvesTo": 119},  # Goldeen -> Seaking
        "119": {"evolvesFrom": 118, "evolvesTo": None},  # Seaking (final stage)
        "120": {"evolvesFrom": None, "evolvesTo": 121},  # Staryu -> Starmie
        "121": {"evolvesFrom": 120, "evolvesTo": None},  # Starmie (final stage)
        "122": {"evolvesFrom": None, "evolvesTo": None},  # Mr. Mime (no evolution)
        "123": {"evolvesFrom": None, "evolvesTo": None},  # Scyther (no evolution)
        "124": {"evolvesFrom": None, "evolvesTo": None},  # Jynx (no evolution)
        "125": {"evolvesFrom": None, "evolvesTo": None},  # Electabuzz (no evolution)
        "126": {"evolvesFrom": None, "evolvesTo": None},  # Magmar (no evolution)
        "127": {"evolvesFrom": None, "evolvesTo": None},  # Pinsir (no evolution)
        "128": {"evolvesFrom": None, "evolvesTo": None},  # Tauros (no evolution)
        "129": {"evolvesFrom": None, "evolvesTo": 130},  # Magikarp -> Gyarados
        "130": {"evolvesFrom": 129, "evolvesTo": None},  # Gyarados (final stage)
        "131": {"evolvesFrom": None, "evolvesTo": None},  # Lapras (no evolution)
        "132": {"evolvesFrom": None, "evolvesTo": None},  # Ditto (no evolution)
        "133": {"evolvesFrom": None, "evolvesTo": 134},  # Eevee -> Vaporeon
        "134": {"evolvesFrom": 133, "evolvesTo": None},  # Vaporeon (final stage)
        "135": {"evolvesFrom": 133, "evolvesTo": None},  # Jolteon (final stage)
        "136": {"evolvesFrom": 133, "evolvesTo": None},  # Flareon (final stage)
        "137": {"evolvesFrom": None, "evolvesTo": None},  # Porygon (no evolution)
        "138": {"evolvesFrom": None, "evolvesTo": 139},  # Omanyte -> Omastar
        "139": {"evolvesFrom": 138, "evolvesTo": None},  # Omastar (final stage)
        "140": {"evolvesFrom": None, "evolvesTo": 141},  # Kabuto -> Kabutops
        "141": {"evolvesFrom": 140, "evolvesTo": None},  # Kabutops (final stage)
        "142": {"evolvesFrom": None, "evolvesTo": None},  # Aerodactyl (no evolution)
        "143": {"evolvesFrom": None, "evolvesTo": None},  # Snorlax (no evolution)
        "144": {"evolvesFrom": None, "evolvesTo": None},  # Articuno (no evolution)
        "145": {"evolvesFrom": None, "evolvesTo": None},  # Zapdos (no evolution)
        "146": {"evolvesFrom": None, "evolvesTo": None},  # Moltres (no evolution)
        "147": {"evolvesFrom": None, "evolvesTo": 148},  # Dratini -> Dragonair
        "148": {"evolvesFrom": 147, "evolvesTo": 149},  # Dragonair -> Dragonite
        "149": {"evolvesFrom": 148, "evolvesTo": None},  # Dragonite (final stage)
        "150": {"evolvesFrom": None, "evolvesTo": None},  # Mewtwo (no evolution)
        "151": {"evolvesFrom": None, "evolvesTo": None},  # Mew (no evolution)
        "280": {"evolvesFrom": None, "evolvesTo": 281},  # Ralts -> Kirlia
        "281": {"evolvesFrom": 280, "evolvesTo": 282},  # Kirlia -> Gardevoir
        "282": {"evolvesFrom": 281, "evolvesTo": None},  # Gardevoir (final stage)
        "303": {"evolvesFrom": None, "evolvesTo": None},  # Mawile (no evolution)
        "522": {"evolvesFrom": None, "evolvesTo": 523},  # Blitzle -> Zebstrika
        "523": {"evolvesFrom": 522, "evolvesTo": None},  # Zebstrika (final stage)
        "527": {"evolvesFrom": None, "evolvesTo": 528},  # Woobat -> Swoobat
        "528": {"evolvesFrom": 527, "evolvesTo": None},  # Swoobat (final stage)
        "546": {"evolvesFrom": None, "evolvesTo": 547},  # Cottonee -> Whimsicott
        "547": {"evolvesFrom": 546, "evolvesTo": None},  # Whimsicott (final stage)
        "549": {"evolvesFrom": None, "evolvesTo": None},  # Lilligant (no evolution)
        "572": {"evolvesFrom": None, "evolvesTo": 573},  # Minccino -> Cinccino
        "573": {"evolvesFrom": 572, "evolvesTo": None},  # Cinccino (final stage)
        "580": {"evolvesFrom": None, "evolvesTo": 581},  # Ducklett -> Swanna
        "581": {"evolvesFrom": 580, "evolvesTo": None},  # Swanna (final stage)
        "602": {"evolvesFrom": None, "evolvesTo": 603},  # Tynamo -> Eelektrik
        "603": {"evolvesFrom": 602, "evolvesTo": 604},  # Eelektrik -> Eelektross
        "604": {"evolvesFrom": 603, "evolvesTo": None},  # Eelektross (final stage)
        "619": {"evolvesFrom": None, "evolvesTo": 620},  # Mienfoo -> Mienshao
        "620": {"evolvesFrom": 619, "evolvesTo": None},  # Mienshao (final stage)
        "622": {"evolvesFrom": None, "evolvesTo": 623},  # Golett -> Golurk
        "623": {"evolvesFrom": 622, "evolvesTo": None},  # Golurk (final stage)
        "624": {"evolvesFrom": None, "evolvesTo": 625},  # Pawniard -> Bisharp
        "625": {"evolvesFrom": 624, "evolvesTo": None},  # Bisharp (final stage)
        "631": {"evolvesFrom": None, "evolvesTo": None},  # Heatmor (no evolution)
        "656": {"evolvesFrom": None, "evolvesTo": 657},  # Froakie -> Frogadier
        "657": {"evolvesFrom": 656, "evolvesTo": 658},  # Frogadier -> Greninja
        "658": {"evolvesFrom": 657, "evolvesTo": None},  # Greninja (final stage)
        "694": {"evolvesFrom": None, "evolvesTo": 695},  # Helioptile -> Heliolisk
        "695": {"evolvesFrom": 694, "evolvesTo": None},  # Heliolisk (final stage)
        "757": {"evolvesFrom": None, "evolvesTo": 758},  # Salandit -> Salazzle
        "758": {"evolvesFrom": 757, "evolvesTo": None},  # Salazzle (final stage)
        "771": {"evolvesFrom": None, "evolvesTo": None},  # Pyukumuku (no evolution)
        "779": {"evolvesFrom": None, "evolvesTo": None},  # Bruxish (no evolution)
        "808": {"evolvesFrom": None, "evolvesTo": 809},  # Meltan -> Melmetal
        "809": {"evolvesFrom": 808, "evolvesTo": None},  # Melmetal (final stage)
        "831": {"evolvesFrom": None, "evolvesTo": 832},  # Wooloo -> Dubwool
        "832": {"evolvesFrom": 831, "evolvesTo": None},  # Dubwool (final stage)
        "850": {"evolvesFrom": None, "evolvesTo": 851},  # Sizzlipede -> Centiskorch
        "851": {"evolvesFrom": 850, "evolvesTo": None},  # Centiskorch (final stage)
        "852": {"evolvesFrom": None, "evolvesTo": 853},  # Clobbopus -> Grapploct
        "853": {"evolvesFrom": 852, "evolvesTo": None},  # Grapploct (final stage)
        "871": {"evolvesFrom": None, "evolvesTo": None},  # Pincurchin (no evolution)
        "872": {"evolvesFrom": None, "evolvesTo": 873},  # Snom -> Frosmoth
        "873": {"evolvesFrom": 872, "evolvesTo": None},  # Frosmoth (final stage)
    }
    return evolution_map.get(cardDexNumber, None)


def edit_card(card):
    evolution_data = map_evolution(str(card["nationalPokedexNumber"]))

    if evolution_data:
        card.update(
            {
                "evolvesFrom": evolution_data["evolvesFrom"],
                "evolvesTo": evolution_data["evolvesTo"],
            }
        )
    else:
        card.update({"evolvesFrom": None, "evolvesTo": None})

    return card


if __name__ == "__main__":
    data = load_json("upload_cards.json")

    if data is None:
        print("Failed to load JSON data")
        exit(1)

    edited_cards = []

    for card in data:
        edited_card = edit_card(card)
        edited_cards.append(edited_card)

    output = "upload_cards2.json"
    with open(output, "w") as file:
        json.dump(edited_cards, file, indent=4)

    print("edited cards")
