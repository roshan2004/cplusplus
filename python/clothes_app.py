from helper_functions import process_csv_supplies
from collections import deque

#The first row is skipped since it only contains labels

csv_data = process_csv_supplies()[1:]

supplies_deque = deque()
for item in csv_data:
    if item[-1] == 'important':
        supplies_deque.appendleft(item)

    else:
        supplies_deque.append(item)

ordered_important_supplies = deque()
ordered_unimportant_supplies = deque()

for _ in range(25):
    ordered_important_supplies.append(supplies_deque.popleft())

for _ in range(10):
    ordered_unimportant_supplies.append(supplies_deque.pop())

print(ordered_important_supplies)
print(ordered_unimportant_supplies)