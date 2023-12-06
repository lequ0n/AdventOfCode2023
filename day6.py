from math import ceil, floor

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# 1
times = list(map(int, data[0].split(':')[1].split()))
distances = list(map(int, data[1].split(':')[1].split()))
prod_ways = 1
for time, distance in zip(times, distances):
    delta = time * time - 4 * distance
    if delta < 0:
        prod_ways *= 0
    else:
        x1 = ceil((-time + delta**0.5) / (-2))
        x2 = floor((-time - delta**0.5) / (-2))
        prod_ways *= (min(time, x2) - max(0, x1) + 1)
print(prod_ways)

# 2
time = int(''.join(data[0].split(':')[1].split()))
distance = int(''.join(data[1].split(':')[1].split()))
num_ways = 0
delta = time * time - 4 * distance
if delta >= 0:
    x1 = ceil((-time + delta**0.5) / (-2))
    x2 = floor((-time - delta**0.5) / (-2))
    num_ways = min(time, x2) - max(0, x1) + 1
print(num_ways)
