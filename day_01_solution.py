floor_count = 0
basement_yet = False
with open("day_01_input.txt", 'r') as brackets_file:
    brackets = brackets_file.readline()
for itr, bracket in enumerate(brackets):
    if bracket == "(":
        floor_count += 1
    elif bracket == ")":
        floor_count -= 1
    if floor_count < 0 and not basement_yet:
        print("Entering basement:", (itr + 1))
        basement_yet = True

print(floor_count)
