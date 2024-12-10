
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class BlockGroup:
    file_id: Optional[int] = None
    size: int = 0
    is_free_space: bool = False

@dataclass
class Block:
    file_id: Optional[int] = None
    is_free_space: bool = False
    def __repr__(self):
        if self.is_free_space:
            return '.'
        return str(self.file_id)

def get_blocks(disk_map: [BlockGroup]):
  blocks = []
  for block_group in disk_map:
    for i in range(block_group.size):
        blocks.append(Block(block_group.file_id, block_group.is_free_space))
  return blocks

def get_checksum(blocks: [Block]):
  return sum([block.file_id * i for i, block in enumerate(blocks) if block.file_id is not None])

def get_disk_map():
    disk_map: [BlockGroup] = []
    with open('input.txt', 'r') as file:
        line = file.readline().strip()
        for i in range(0, len(line), 2):
            disk_map.append(
                BlockGroup(
                    int(i / 2),
                    int(line[i]),
                    False
                )
            )
            if i < len(line) - 1:
                disk_map.append(
                    BlockGroup(
                        None,
                        int(line[i + 1]),
                        True
                    )
                )
    return disk_map

# Part 1

blocks = get_blocks(get_disk_map())

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

block_groups = get_disk_map()

print(get_blocks(block_groups))

for i in range(len(block_groups) - 1, -1, -1):
    if block_groups[i].file_id is not None:
        for j in range(len(block_groups)):
            if (
                block_groups[j].is_free_space
                and block_groups[j].size >= block_groups[i].size
            ):
                new_free_block_groups = (
                    BlockGroup(
                        None,
                        block_groups[i].size,
                        True
                    ),
                    BlockGroup(
                        None,
                        block_groups[i].size - block_groups[j].size,
                        True
                    )
                )
                if new_free_block_groups[1].size > 0:
                    block_groups[j] = new_free_block_groups[0]
                    block_groups.insert(j + 1, new_free_block_groups[1])
                block_groups[j], block_groups[i] = block_groups[i], block_groups[j]

blocks = get_blocks(block_groups)

print(blocks)

checksum = get_checksum(blocks)

end_time = datetime.now()

print('Part 2 Checksum:', checksum)
print('Part 2 executed in:', (end_time - start_time).total_seconds(), 'seconds.')
