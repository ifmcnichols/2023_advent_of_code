input_file = open("day_03_input.txt", "r")
lines = input_file.readlines()
input_file.close()


def check_number(first_index, current_line, prev_line, next_line, number):
    last_index = first_index + len(obj) - 1
    if number[0] != current_line[first_index]:
        breakpoint()
    if prev_line is not None:
        for i in prev_line[first_index-1:last_index+2]:
            if i != "." and not i.isdigit():
                return True
    if next_line is not None:
        for i in next_line[first_index-1:last_index+2]:
            if i != "." and not i.isdigit():
                return True
    if current_line[first_index-1] != "." and not current_line[last_index+1].isdigit():
        return True

    return False


parts_sum = 0


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
            idx += len(obj) + 1
            if is_part:
                #print("adding number: ", obj)
                #print(previous)
                #print(current)
                #print(next)
                #print("===========\n")
                parts_sum += int(obj)
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
                print("adding number: ", obj)
                print(previous)
                print(current)
                print(next)
                print("===========\n")
            else:
                middle_thing = [x.isdigit() for x in obj].index(False)
                obj1 = obj[0:middle_thing]
                obj2 = obj[middle_thing+1:]
                obj = int(obj1) + int(obj2)
                print("adding numbers: ", obj1, obj2)
                print(previous)
                print(current)
                print(next)
                print("===========\n")

            parts_sum += int(obj)
            idx += orig_length + 1

print("sum:", parts_sum)
