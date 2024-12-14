garden = [list(line.strip()) for line in open('input.txt')]

def walk_garden(garden, plot: tuple[int, int], visited_plots):
    x, y = plot
    region = [plot]
    visited_plots.add(plot)

    # up
    if (
        y > 0
        and garden[y - 1][x] not in visited_plots
        and garden[y - 1][x] == garden[y][x]
    ):
        visited_plots.add((x, y - 1))
        region.append((x, y - 1))
        region += walk_garden(garden, (x, y - 1), visited_plots)
    #right
    if (
        x < len(garden[y]) - 1
        and garden[y][x + 1] not in visited_plots
        and garden[y][x + 1] == garden[y][x]
    ):
        visited_plots.add((x + 1, y))
        region.append((x + 1, y))
        region += walk_garden(garden, (x + 1, y), visited_plots)
    # down
    if (
        y < len(garden) - 1
        and garden[y + 1][x] not in visited_plots
        and garden[y + 1][x] == garden[y][x]
    ):
        visited_plots.add((x, y + 1))
        region.append((x, y + 1))
        region += walk_garden(garden, (x, y + 1), visited_plots)
    # left
    if (
        x > 0
        and garden[y][x - 1] not in visited_plots
        and garden[y][x - 1] == garden[y][x]
    ):
        visited_plots.add((x - 1, y))
        region.append((x - 1, y))
        region += walk_garden(garden, (x - 1, y), visited_plots)
    return region


regions : [[(int, int)]] = []
visited_plots: set[tuple[int, int]] = set()

for y in range(len(garden)):
    for x in range(len(garden[y])):
        if (x, y) not in visited_plots:
            regions.append(walk_garden(garden, (x, y), visited_plots))

print(len(regions), 'regions')
print(regions)
    
