input_file = open("day_03_input.txt", "r")
lines = input_file.readlines()
input_file.close()
from termcolor import colored


def check_number(first_index, current_line, prev_line, next_line, number):
    la_in = first_index + len(obj) - 1
    fi_in = first_index
    if number[0] != current_line[first_index]:
        breakpoint()
    if fi_in == 0:
        first_index += 1
    if prev_line is not None:
        for i in prev_line[fi_in-1:la_in+2]:
            if i != "." and not i.isdigit():
                return True
    if next_line is not None:
        for i in next_line[fi_in-1:la_in+2]:
            if i != "." and not i.isdigit():
                return True
    if current_line[fi_in-1] != "." and not current_line[la_in+1].isdigit():
        return True

    print(colored("skipping number:", 'red'), number)
    if prev_line is not None:
        print(prev_line[fi_in-1:la_in+2])
    print(current_line[fi_in-1:la_in+2])
    if next_line is not None:
        print(next_line[fi_in-1:la_in+2])
    print("===========\n")
    return False


parts_sum = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", ".")

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
    print("=======")
    for obj in line:
        if obj == "":
            idx += 1
        elif obj.isdigit():
            is_part = check_number(idx, current, previous, next, obj)
            if is_part:
                print(colored("adding number: ", 'green'), obj)
                if previous is not None:
                    print(previous[idx-1:idx+len(obj)+1])
                print(current[idx-1:idx+len(obj)+1])
                if next is not None:
                    print(next[idx-1:idx+len(obj)+1])
                print("===========\n")
                parts_sum += int(obj)
            idx += len(obj) + 1
        elif len(obj) == 1:
            idx += 2
        else:
            orig_length = len(obj)
            orig_obj = obj
            if len(obj) <= 4:
                for thing in obj:
                    if not thing.isdigit():
                        reason = thing
                        obj = obj.replace(thing, "")
                print(colored("adding number: ", 'green'), obj)
                if previous is not None:
                    print(previous[idx-1:idx+len(obj)+1])
                print(current[idx-1:idx+len(obj)+1])
                if next is not None:
                    print(next[idx-1:idx+len(obj)+1])
                print("===========\n")
            else:
                middle_thing = [x.isdigit() for x in obj].index(False)
                obj1 = obj[0:middle_thing]
                obj2 = obj[middle_thing+1:]
                obj = int(obj1) + int(obj2)
                print(colored("adding number: ", 'green'), obj1, obj2)
                if previous is not None:
                    print(previous[idx-1:idx+orig_length+1])
                print(current[idx-1:idx+orig_length+1])
                if next is not None:
                    print(next[idx-1:idx+orig_length+1])
                print("===========\n")

            parts_sum += int(obj)
            idx += orig_length + 1

print("sum:", parts_sum)
