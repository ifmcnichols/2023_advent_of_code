nums_dict_forward = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
nums_dict_backward = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "rouf": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
    "net": 10
}


def get_first_digit(entry):
    while True:
        for x in entry:
            if x.isdigit():
                return str(x)


calibration_sum = 0

inputs = open("day_01_input.txt", "r")
lines = inputs.readlines()
inputs.close()

for line in lines:
    line = line.strip()
    first_digit = get_first_digit(line)
    last_digit = get_first_digit(line[::-1])
    total = int(first_digit + last_digit)
    calibration_sum += total

print("sum:", calibration_sum)


def get_first_digit_pt2(entry, forward=True):
    if forward:
        nums_dict = nums_dict_forward
    else:
        nums_dict = nums_dict_backward
    for i in range(len(entry)):
        if entry[i].isdigit():
            return entry[i]
        else:
            for j in range(0, i):
                if entry[j:i+1] in nums_dict.keys():
                    return str(nums_dict[entry[j:i+1]])


def fill_w_digits(full_string):
    full_string = full_string.replace("one", "o1e")
    full_string = full_string.replace("two", "t2o")
    full_string = full_string.replace("three", "t3e")
    full_string = full_string.replace("four", "f4r")
    full_string = full_string.replace("five", "f5e")
    full_string = full_string.replace("six", "s6x")
    full_string = full_string.replace("seven", "s7n")
    full_string = full_string.replace("eight", "e8t")
    full_string = full_string.replace("nine", "n9n")
    return full_string


calibration_sum = 0
inputs = open("day_01_input.txt", "r")
lines = inputs.readlines()
inputs.close()

for line in lines:
    line = line.strip()
    line = fill_w_digits(line)
    first_digit = get_first_digit(line)
    last_digit = get_first_digit(line[::-1])
    total = int(first_digit + last_digit)
    calibration_sum += total


print("sum:", calibration_sum)
