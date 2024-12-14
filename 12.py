garden = [list(line.strip()) for line in open('input.txt')]

def get_regions(garden):
    regions = []
    visited_plots = set()
    
    for y in range(len(garden)):
        for x in range(len(garden[y])):
            if (x, y) not in visited_plots:
                region = walk_garden(garden, (x, y), visited_plots)
                regions.append(region)

    return regions

def walk_garden(garden, plot, visited_plots):
    x, y = plot
    region = [plot]
    visited_plots.add(plot)

    # up
    if (
        y > 0
        and (x, y - 1) not in visited_plots
        and garden[y - 1][x] == garden[y][x]
    ):
        region += walk_garden(garden, (x, y - 1), visited_plots)
    # right
    if (
        x < len(garden[y]) - 1
        and (x + 1, y) not in visited_plots
        and garden[y][x + 1] == garden[y][x]
    ):
        region += walk_garden(garden, (x + 1, y), visited_plots)
    # down
    if (
        y < len(garden) - 1
        and (x, y + 1) not in visited_plots
        and garden[y + 1][x] == garden[y][x]
    ):
        region += walk_garden(garden, (x, y + 1), visited_plots)
    # left
    if (
        x > 0
        and (x - 1, y) not in visited_plots
        and garden[y][x - 1] == garden[y][x]
    ):
        region += walk_garden(garden, (x - 1, y), visited_plots)
    
    return region

def calculate_perimeter(region):
    perimeter = 0
    for plot in region:
        x, y = plot
        if y == 0 or garden[y - 1][x] != garden[y][x]:
            perimeter += 1
        if x == len(garden[y]) - 1 or garden[y][x + 1] != garden[y][x]:
            perimeter += 1
        if y == len(garden) - 1 or garden[y + 1][x] != garden[y][x]:
            perimeter += 1
        if x == 0 or garden[y][x - 1] != garden[y][x]:
            perimeter += 1
    return perimeter

def get_region_matrix(region):
    min_x = min(plot[0] for plot in region)
    max_x = max(plot[0] for plot in region)
    min_y = min(plot[1] for plot in region)
    max_y = max(plot[1] for plot in region)

    matrix = [['' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for plot in region:
        x, y = plot
        matrix[y - min_y][x - min_x] = garden[y][x]

    return matrix    

def has_plot_on_the_left(region_matrix, x, y):
    return x != 0 and region_matrix[y][x - 1] != ''

def has_plot_on_the_right(region_matrix, x, y):
    return x != len(region_matrix[0]) - 1 and region_matrix[y][x + 1] != ''

def has_left_side(region_matrix, x, y):
    return not has_plot_on_the_left(region_matrix, x, y) and has_plot_on_the_right(region_matrix, x, y)

def has_right_side(region_matrix, x, y):
    return has_plot_on_the_left(region_matrix, x, y) and not has_plot_on_the_right(region_matrix, x, y)

def has_plot_above(region_matrix, x, y):
    return y != 0 and region_matrix[y - 1][x] != ''

def has_plot_below(region_matrix, x, y):
    return y != len(region_matrix) - 1 and region_matrix[y + 1][x] != ''

def has_top_side(region_matrix, x, y):
    return not has_plot_above(region_matrix, x, y) and has_plot_below(region_matrix, x, y)

def has_bottom_side(region_matrix, x, y):
    return has_plot_above(region_matrix, x, y) and not has_plot_below(region_matrix, x, y)

def count_sides(region):
    region_matrix = get_region_matrix(region)
    sides = 0

    # Check for vertical sides
    for x in range(len(region_matrix[0])):
        for y in range(len(region_matrix)):
            above_has_left_side = y != 0 and has_left_side(region_matrix, x, y - 1)
            above_has_right_side = y != 0 and has_right_side(region_matrix, x, y - 1)
            if has_left_side(region_matrix, x, y) and not above_has_left_side:
                sides += 1
            if has_right_side(region_matrix, x, y) and not above_has_right_side:
                sides += 1

    # Check for horizontal sides
    for y in range(len(region_matrix)):
        for x in range(len(region_matrix[0])):
            left_has_top_side = x != 0 and has_top_side(region_matrix, x - 1, y)
            left_has_bottom_side = x != 0 and has_bottom_side(region_matrix, x - 1, y)
            if has_top_side(region_matrix, x, y) and not left_has_top_side:
                sides += 1
            if has_bottom_side(region_matrix, x, y) and not left_has_bottom_side:
                sides += 1

    return sides
        

regions = get_regions(garden)

total_price = 0
for region in regions:
    perimeter = calculate_perimeter(region)
    area = len(region)
    total_price += area * perimeter

print('Total price (part 1):', total_price)

total_price = 0
for region in regions:
    sides = count_sides(region)
    print('Region:', garden[region[0][1]][region[0][0]], 'Sides:', sides)
    area = len(region)
    total_price += area * sides

print('Total price (part 2):', total_price)
