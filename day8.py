from math import lcm

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    instructions = data[0]
    data = [line.split('=') for line in data[2:]]
    nodes = {key.strip(): [val.split(',')[0].strip(' ('), val.split(',')[1].strip(' )')] for key, val in data}

# 1
steps = 0
current_node = 'AAA'
final_node = 'ZZZ'
while current_node != final_node:
    current_node = nodes[current_node][0] if instructions[steps % len(instructions)] == 'L' else nodes[current_node][1]
    steps += 1
print(steps)

# 2
# This solution probably won't work for all inputs
steps = 1
for node in [node for node in nodes if node.endswith('A')]:
    sub_steps = 0
    while not node.endswith('Z'):
        node = nodes[node][0] if instructions[sub_steps % len(instructions)] == 'L' else nodes[node][1]
        sub_steps += 1
    steps = lcm(steps, sub_steps)
print(steps)
