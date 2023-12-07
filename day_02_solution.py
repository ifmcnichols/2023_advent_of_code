def calc_surface_area(length, width, height):
    length = int(length)
    width = int(width)
    height = int(height)
    sa = (2*length*width) + (2*width*height) + (2*height*length)
    min_side = min([length, width, height])
    return sa + min_side


total_sqft = 0

with open("day_02_input.txt") as presents_file:
    for line in presents_file.readlines():
        l, w, h = line.split("x")
        total_sqft += calc_surface_area(l, w, h)
print('total sqft:', total_sqft)
