import json

def save_game(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)  # indent=4 makes it readable

def load_game(filename):
    with open(filename, "r") as f:
        return json.load(f)


game_data = {
    "player": {"name": "Alice", "level": 5, "hp": 100},
    "inventory": ["sword", "shield"],
    "position": {"x": 10, "y": 5}
}

save_game("save1.json", game_data)

loaded = load_game("save1.json")
print(loaded)
