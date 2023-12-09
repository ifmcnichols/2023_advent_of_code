def clean_input():
    # Winning cards are index 0
    # My cards are index 1
    output = []
    with open("day_04_input.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.strip()
            winning = line.split("|")[0].split(": ")[1].split(" ")
            while "" in winning:
                winning.remove("")
            mine = line.split("|")[1].split(" ")
            while "" in mine:
                mine.remove("")
            output.append((set(winning), set(mine)))
    return output

x = clean_input()

sum_total = 0
for line in x:
    winning_cards = len(line[0].intersection(line[1]))
    if winning_cards > 0:
        sum_total += 2 ** (winning_cards-1)

print("sum:", sum_total)
