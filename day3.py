with open('input.txt', 'r') as f:
    data = f.read().splitlines()

data.insert(0, '.' * (len(data[0]) + 2))
data.append(data[0])
for i in range(1, len(data) - 1):
    data[i] = '.' + data[i] + '.'

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

# 1
part_numbers_sum = 0
for i, row in enumerate(data):
    starts = [j for j, char in enumerate(row) if char in digits and row[j - 1] not in digits]
    ends = [j for j, char in enumerate(row) if char in digits and row[j + 1] not in digits]
    for start, end in zip(starts, ends):
        neighbors = [x for x in data[i - 1][start - 1:end + 2]] + [x for x in data[i + 1][start - 1:end + 2]
                                                                   ] + [row[start - 1], row[end + 1]]
        if any(x not in digits and x != '.' for x in neighbors): part_numbers_sum += int(row[start:end + 1])
print(part_numbers_sum)

# 2
gear_ratio_sum = 0
for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char == '*':
            attached_parts = []
            for k in [-1, 1]:
                if row[(p := j + k)] in digits:
                    while row[p] in digits:
                        p += k
                    attached_parts.append(int(row[min(p + 1, j + 1):max(j, p)]))
            for k in [i - 1, i + 1]:
                l, r = j - 1, j + 1
                while data[k][l] in digits:
                    l -= 1
                while data[k][r] in digits:
                    r += 1
                if data[k][j] in digits: attached_parts.append(int(data[k][l + 1:r]))
                else:
                    if l != j - 1: attached_parts.append(int(data[k][l + 1:j]))
                    if r != j + 1: attached_parts.append(int(data[k][j + 1:r]))
            if len(attached_parts) == 2: gear_ratio_sum += attached_parts[0] * attached_parts[-1]
print(gear_ratio_sum)
