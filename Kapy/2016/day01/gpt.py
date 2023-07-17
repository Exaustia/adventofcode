def calculate_distance(instructions):
    # Initialize position and direction variables
    x, y = 0, 0
    direction = 0  # 0: North, 1: East, 2: South, 3: West

    # Split the instructions by commas and remove any whitespace
    instructions = instructions.replace(',', '').split()

    for instruction in instructions:
        # Extract the turn direction and number of blocks
        turn = instruction[0]
        blocks = int(instruction[1:])

        # Update the direction based on the turn
        if turn == 'R':
            direction = (direction + 1) % 4
        elif turn == 'L':
            direction = (direction - 1) % 4

        # Update the position based on the direction and blocks
        if direction == 0:
            y += blocks
        elif direction == 1:
            x += blocks
        elif direction == 2:
            y -= blocks
        elif direction == 3:
            x -= blocks

    # Calculate the Manhattan distance to the destination
    distance = abs(x) + abs(y)
    return distance

# Example usage:
instructions = "R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5"
distance = calculate_distance(instructions)
print("The distance to Easter Bunny HQ is", distance, "blocks.")