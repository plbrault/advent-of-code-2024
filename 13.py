import numpy as np

def parse_file(filename):
    machines = []
    with open(filename, 'r') as file:
        machine_configs = file.read().split('\n\n')
        for machine_config in machine_configs:
            lines = machine_config.split('\n')
            button_a = lines[0].split(':')[1].strip()
            button_a_x = button_a.split(',')[0].split('+')[1]
            button_a_y = button_a.split(',')[1].split('+')[1]
            button_b = lines[1].split(':')[1].strip()
            button_b_x = button_b.split(',')[0].split('+')[1]
            button_b_y = button_b.split(',')[1].split('+')[1]
            prize = lines[2].split(':')[1].strip()
            prize_x = prize.split(',')[0].split('=')[1]
            prize_y = prize.split(',')[1].split('=')[1]

            machine = {
                'a': (int(button_a_x), int(button_a_y)),
                'b': (int(button_b_x), int(button_b_y)),
                'prize': (int(prize_x), int(prize_y))
            }
            machines.append(machine)
    return machines

def calculate_tokens(machines, max_button_presses=float('inf')):
    tokens = 0
    for machine in machines:
        a, b = np.linalg.solve(
            [
                [machine['a'][0], machine['b'][0]],
                [machine['a'][1], machine['b'][1]]
            ],
            [machine['prize'][0], machine['prize'][1]]
        )

        if 0 <= a <= max_button_presses and 0 <= b <= max_button_presses:
            a = int(round(a))
            b = int(round(b))
            if (
                machine['a'][0] * a + machine['b'][0] * b == machine['prize'][0] and
                machine['a'][1] * a + machine['b'][1] * b == machine['prize'][1]
            ):
                tokens += 3 * a + b
    return tokens

# Part 1
machines = parse_file('input.txt')
tokens = calculate_tokens(machines, 100)
print('Number of tokens (part 1):', tokens)

# Part 2
for machine in machines:
    value_to_add = 10000000000000
    machine['prize'] = (
        machine['prize'][0] + value_to_add,
        machine['prize'][1] + value_to_add
    )
tokens = calculate_tokens(machines)
print('Number of tokens (part 2):', tokens)
