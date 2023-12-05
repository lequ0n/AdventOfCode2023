from collections import deque

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# 1
seeds = list(map(int, data[0].split(':')[1].split()))
i = 1
while i < len(data):
    mapping = []
    i += 2
    while i < len(data) and data[i]:
        destination, source, range_length = map(int, data[i].split())
        mapping.append((source, destination, range_length))
        i += 1
    mapped_values = []
    for x in seeds:
        for source, destination, range_length in mapping:
            if source <= x < source + range_length:
                x = destination + x - source
                break
        mapped_values.append(x)
    seeds = mapped_values
print(min(seeds))

# 2
seeds = [
    list(map(int, data[0].split(':')[1].split()[i:i + 2])) for i in range(0, len(data[0].split(':')[1].split()), 2)
]
i = 1
while i < len(data):
    mapping = []
    i += 2
    while i < len(data) and data[i]:
        destination, source, range_length = map(int, data[i].split())
        mapping.append((source, destination, range_length))
        i += 1
    mapped_values = []
    for start, length in seeds:
        q = deque([(start, start + length - 1)])
        while q:
            l, r = q.popleft()
            for source, destination, range_length in mapping:
                if source <= l <= r < source + range_length:
                    mapped_values.append((destination + l - source, r - l + 1))
                    break
                elif l < source and r >= source + range_length:
                    mapped_values.append((destination, range_length))
                    q.append((l, source - 1))
                    q.append((source + range_length, r))
                    break
                elif l < source <= r < source + range_length:
                    mapped_values.append((destination, r - source + 1))
                    q.append((l, source - 1))
                    break
                elif source <= l < source + range_length <= r:
                    mapped_values.append((destination + l - source, source + range_length - l))
                    q.append((source + range_length, r))
                    break
            else:
                mapped_values.append((l, r - l + 1))
    seeds = mapped_values
print(min(seeds)[0])
