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
            print(f'Button A: ({button_a_x}, {button_a_y})')
            print(f'Button B: ({button_b_x}, {button_b_y})')
            print(f'Prize: ({prize_x}, {prize_y})')

            machine = {
                'a': (int(button_a_x), int(button_a_y)),
                'b': (int(button_b_x), int(button_b_y)),
                'prize': (int(prize_x), int(prize_y))
            }
            machines.append(machine)
    return machines

machines = parse_file('input.txt')
print(machines)
