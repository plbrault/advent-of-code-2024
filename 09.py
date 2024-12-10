
from dataclasses import dataclass
from typing import Optional

disk_map: list[int]

with open('input.txt', 'r') as file:
    first_line = file.readline().strip()
    disk_map = [int(number) for number in first_line]

@dataclass
class Block:
    file_id: Optional[int] = None
    is_free_space: bool = False
    def __repr__(self):
        if self.is_free_space:
            return '.'
        return str(self.file_id)

blocks = []

for i in range(0, len(disk_map), 2):
    for j in range(disk_map[i]):
        blocks.append(Block(file_id=int(i/2)))
    if i + 1 < len(disk_map):
        for j in range(disk_map[i+1]):
            blocks.append(Block(is_free_space=True))

previous_free_block_id = 0
for i in range(len(blocks) - 1, -1, -1):
    if not blocks[i].is_free_space:
        for j in range(previous_free_block_id, i):
          if blocks[j].is_free_space:
            blocks[i], blocks[j] = blocks[j], blocks[i]
            previous_free_block_id = j
            break

checksum = sum([block.file_id * i for i, block in enumerate(blocks) if block.file_id is not None])

print('Checksum:', checksum)
