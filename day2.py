from numpy import prod

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# 1
bag_contents = (12, 13, 14)
ids_sum = 0
for i, line in enumerate(data, start=1):
    cube_sets = line.split(':')[1].strip().split(';')
    for cube_set in cube_sets:
        d = {'red': 0, 'green': 0, 'blue': 0}
        cube_set = cube_set.strip().split(',')
        for part in cube_set:
            num, color = part.split()
            d[color] += int(num)
        if any(d[color] > bag_contents[i] for i, color in enumerate(d)):
            break
    else:
        ids_sum += i
print(ids_sum)

# 2
power_sum = 0
for line in data:
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    cube_sets = line.split(':')[1].strip().split(';')
    for cube_set in cube_sets:
        d = {'red': 0, 'green': 0, 'blue': 0}
        cube_set = cube_set.strip().split(',')
        for part in cube_set:
            num, color = part.split()
            d[color] += int(num)
        for color in d:
            min_cubes[color] = max(min_cubes[color], d[color])
    power_sum += prod(list(min_cubes.values()))
print(power_sum)
