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

def count_sides(region):
    region_matrix = get_region_matrix(region)

    return 0

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