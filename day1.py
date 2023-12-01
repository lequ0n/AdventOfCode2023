import re

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# 1
print(sum(10 * int((t := re.sub(r"\D", '', line))[0]) + int(t[-1]) for line in data))

# 2
mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
print(
    sum(10 * mapping[(t := re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line))[0]] +
        mapping[t[-1]] for line in data))
