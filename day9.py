with open('input.txt') as f:
    lines = [list(map(int, line.split())) for line in f.read().splitlines()]

# 1
extrapolated_values_sum = 0
for line in lines:
    differences = [line]
    while any(x != 0 for x in differences[-1]):
        current_step_differences = []
        for i in range(len(differences[-1]) - 1):
            current_step_differences.append(differences[-1][i + 1] - differences[-1][i])
        differences.append(current_step_differences)
        if len(differences[-1]) == 1 and differences[-1][0] != 0:
            differences.append([0])
    differences[-1].append(0)
    for i in range(len(differences) - 2, -1, -1):
        differences[i].append(differences[i][-1] + differences[i + 1][-1])
    extrapolated_values_sum += differences[0][-1]
print(extrapolated_values_sum)

# 2
extrapolated_values_sum = 0
for line in lines:
    differences = [line]
    while any(x != 0 for x in differences[-1]):
        current_step_differences = []
        for i in range(len(differences[-1]) - 1):
            current_step_differences.append(differences[-1][i + 1] - differences[-1][i])
        differences.append(current_step_differences)
        if len(differences[-1]) == 1 and differences[-1][0] != 0:
            differences.append([0])
    differences[-1].insert(0, 0)
    for i in range(len(differences) - 2, -1, -1):
        differences[i].insert(0, differences[i][0] - differences[i + 1][0])
    extrapolated_values_sum += differences[0][0]
print(extrapolated_values_sum)