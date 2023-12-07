input_file = open("day_03_input.txt", "r")
lines = input_file.readlines()
input_file.close()


def check_number(first_index, last_index, current_line, prev_line, next_line, number):
    if prev_line is not None:
        for i in range(first_index-1, last_index+1):
            if prev_line[i] != "." and not prev_line[i].isdigit():
                print("part:", number, "because:", prev_line[i])
                return True
    if next_line is not None:
        for i in range(first_index-1, last_index+1):
            if next_line[i] != "." and not next_line[i].isdigit():
                print("part:", number, "because:", next_line[i])
                return True
    if current_line[first_index] != "." and not current_line[last_index].isdigit():
        return True
    if current_line[first_index] != "." and not current_line[last_index].isdigit():
        return True

    return False

parts_sum = 0

lines = lines[0:5]


for itr, line in enumerate(lines):
    if itr == 0:
        previous = None
    else:
        previous = lines[itr-1].strip()
    if itr == len(lines)-1:
        next = None
    else:
        next = lines[itr+1].strip()
    line = line.strip()
    current = line
    line = line.split(".")
    idx = 0
    for obj in line:
        if obj == "":
            idx += 1
        elif obj.isdigit():
            is_part = check_number(idx, idx+len(obj), current, previous, next, obj)
            idx += len(obj) + 1
            if is_part:
                parts_sum += int(obj)
        elif len(obj) == 1:
            idx += 1
        else:
            orig_length = len(obj)
            for thing in obj:
                if not thing.isdigit():
                    reason = thing
                    obj = obj.replace(thing, "")
            print("part:", obj, "because:", reason)
            parts_sum += int(obj)
            idx += orig_length + 1

print("sum:", parts_sum)
