def clean_input():
    with open("day_03_input.txt", "r") as datafile:
        output = []
        output.append(["." for x in range(142)])
        for line in datafile.readlines():
            line = "." + line.strip() + "."
            output.append(line)
        output.append(["." for x in range(142)])
    return output


def translate_digits(line):
    i = 0
    number = ""
    number_indices = []
    while i < len(line):
        while line[i].isdigit():
            number += line[i]
            i += 1
            continue
        number += ","
        i += 1
    indx = 0
    output = []
    for x in number.split(","):
        if x != "":
            output.append((x, len(x), indx))
            indx += len(x) + 1
        else:
            indx += 1
    return output


x = clean_input()
total = 0

for ii in range(len(x)):
    for jj in range(len(x[ii])):
        if x[ii][jj] == "*":
            sum_list = []
            for digit in translate_digits(x[ii-1]):
                if digit[-1]-1 <= jj <= digit[-1] + digit[1]+1:
                    sum_list.append(digit[0])
            for digit in translate_digits(x[ii]):
                if digit[-1]-1 <= jj <= digit[-1] + digit[1]+1:
                    sum_list.append(digit[0])
            for digit in translate_digits(x[ii+1]):
                if digit[-1]-1 <= jj <= digit[-1] + digit[1]+1:
                    sum_list.append(digit[0])
            if len(sum_list) == 2:
                breakpoint()
                total += (int(sum_list[0])*int(sum_list[1]))
print("Sum:", total)

# 69278118 is too low :(
