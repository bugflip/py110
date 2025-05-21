
def calculate_leftover_blocks(total_blocks):
    layers = []
    blocks_in_structure = 0
    current_layer = 1
    while blocks_in_structure <= total_blocks:
        layers.append(current_layer ** 2)
        blocks_in_structure = sum(layers)
        current_layer += 1
    return total_blocks - sum(layers[:-1])

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
