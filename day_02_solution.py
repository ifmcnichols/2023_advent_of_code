max_reds = 12
max_greens = 13
max_blues = 14


def game_possible(input_dict):
    if input_dict["reds"] > max_reds:
        return False
    if input_dict["blues"] > max_blues:
        return False
    if input_dict["greens"] > max_greens:
        return False
    return True


def parse_line(input_line):
    input_line = input_line.strip()
    game_id = int(input_line.split(":")[0].split(" ")[1])
    reds = 0
    blues = 0
    greens = 0
    for game in input_line.split(";"):
        if "red" in game:
            red = int(game.split(" red")[0].split(" ")[-1])
            if red > reds:
                reds = red
        if "blue" in game:
            blue = int(game.split(" blue")[0].split(" ")[-1])
            if blue > blues:
                blues = blue
        if "green" in game:
            green = int(game.split(" green")[0].split(" ")[-1])
            if green > greens:
                greens = green
    return {"id": game_id, "reds": reds, "greens": greens, "blues": blues}


inputs_file = open("day_02_input.txt", "r")
lines = inputs_file.readlines()
inputs_file.close()

id_sum = 0

for line in lines:
    line_data = parse_line(line)
    possible = game_possible(line_data)
    if possible:
        id_sum += line_data["id"]

print("sum:", id_sum)
