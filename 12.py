garden = [list(line.strip()) for line in open('input.txt')]

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

regions = []
visited_plots = set()

for y in range(len(garden)):
    for x in range(len(garden[y])):
        if (x, y) not in visited_plots:
            region = walk_garden(garden, (x, y), visited_plots)
            regions.append(region)

print(len(regions), 'regions')

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

total_perimeter = 0
for region in regions:
    perimeter = calculate_perimeter(region)
    print('Region:', garden[region[0][1]][region[0][0]], 'Perimeter:', perimeter)
    total_perimeter += calculate_perimeter(region)

print('Total perimeter:', total_perimeter)
