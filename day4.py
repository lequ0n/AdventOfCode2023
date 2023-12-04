with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# 1
total_points = 0
for card in data:
    winning_numbers, your_numbers = card.split(':')[1].split('|')
    winning_numbers = {int(x) for x in winning_numbers.split()}
    your_numbers = {int(x) for x in your_numbers.split()}
    num_common_numbers = len(winning_numbers & your_numbers)
    if num_common_numbers:
        total_points += 2**(num_common_numbers - 1)
print(total_points)

# 2
num_scratchcards = [1 for _ in range(len(data))]
for i, card in enumerate(data):
    winning_numbers, your_numbers = card.split(':')[1].split('|')
    winning_numbers = {int(x) for x in winning_numbers.split()}
    your_numbers = {int(x) for x in your_numbers.split()}
    num_common_numbers = len(winning_numbers & your_numbers)
    for j in range(i + 1, i + 1 + num_common_numbers):
        num_scratchcards[j] += num_scratchcards[i]
print(sum(num_scratchcards))
