
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Block:
    file_id: Optional[int] = None
    file_size: Optional[int] = None
    is_free_space: bool = False
    def __repr__(self):
        if self.is_free_space:
            return '.'
        return str(self.file_id)

def get_blocks(disk_map):
  blocks = []
  for i in range(0, len(disk_map), 2):
      for j in range(disk_map[i]):
          blocks.append(Block(file_id=int(i/2), file_size=disk_map[i]))
      if i + 1 < len(disk_map):
          for j in range(disk_map[i+1]):
              blocks.append(Block(is_free_space=True))
  return blocks

def get_checksum(blocks: [Block]):
  return sum([block.file_id * i for i, block in enumerate(blocks) if block.file_id is not None])

disk_map: list[int]

with open('input.txt', 'r') as file:
    first_line = file.readline().strip()
    disk_map = [int(number) for number in first_line]

# Part 1

blocks = get_blocks(disk_map)

previous_free_block_id = 0
for i in range(len(blocks) - 1, -1, -1):
    if not blocks[i].is_free_space:
        for j in range(previous_free_block_id, i):
          if blocks[j].is_free_space:
            blocks[i], blocks[j] = blocks[j], blocks[i]
            previous_free_block_id = j
            break

checksum = get_checksum(blocks)

print('Part 1 Checksum:', checksum)

# Part 2

start_time = datetime.now()

blocks = get_blocks(disk_map)

last_file_id = -1
first_free_block_idx = 0
for i in range(len(blocks) - 1, -1, -1):
    file_start_idx = None
    if blocks[i].is_free_space:
        if last_file_id > -1:
            file_start_idx = i + 1
            last_file_id = -1
    elif last_file_id == -1:
        last_file_id = blocks[i].file_id
    elif blocks[i].file_id != last_file_id:
        file_start_idx = i + 1
    if file_start_idx != None:
        free_space_start_idx = None
        for j in range(first_free_block_idx, len(blocks)):
            if blocks[j].is_free_space:
                first_free_block_idx = j
                break
        for j in range(first_free_block_idx, len(blocks)):
            if blocks[j].is_free_space:
                free_space_size = 0
                k = j
                while k < len(blocks) and blocks[k].is_free_space:
                    free_space_size += 1
                    k += 1
                if free_space_size >= blocks[file_start_idx].file_size:
                    free_space_start_idx = j
                    break
        for j in range(blocks[file_start_idx].file_size):
            blocks[file_start_idx + j], blocks[free_space_start_idx + j] = blocks[free_space_start_idx + j], blocks[file_start_idx + j]

checksum = get_checksum(blocks)

end_time = datetime.now()

print('Part 2 Checksum:', checksum)
print('Executed in:', (end_time - start_time).total_seconds(), 'seconds.')
