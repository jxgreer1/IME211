import random

# Initialize the grid size
GRID_SIZE = 6
TREASURE_COUNT = 3
TRAP_COUNT = 2

# Player start position
player_pos = [0, 0]

# Generate random positions for treasures and traps
def generate_positions(count):
    positions = []
    while len(positions) < count:
        pos = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        if pos not in positions and pos != player_pos:
            positions.append(pos)
    return positions

treasures = generate_positions(TREASURE_COUNT)
traps = generate_positions(TRAP_COUNT)

def print_grid():
    print("\nTreasure Hunt Grid:")
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if [row, col] == player_pos:
                print("P", end=" ")  # Player
            else:
                print(".", end=" ")  # Empty space
        print()
    print()

def move_player():
    move = input("Move (WASD): ").lower()
    if move == "w" and player_pos[0] > 0:
        player_pos[0] -= 1
    elif move == "s" and player_pos[0] < GRID_SIZE - 1:
        player_pos[0] += 1
    elif move == "a" and player_pos[1] > 0:
        player_pos[1] -= 1
    elif move == "d" and player_pos[1] < GRID_SIZE - 1:
        player_pos[1] += 1
    else:
        print("Invalid move! Try again.")

def check_position():
    if player_pos in treasures:
        treasures.remove(player_pos)
        print("You found a treasure! 🎉")
    elif player_pos in traps:
        print("You stepped on a trap! 💥 Game Over.")
        return False
    return True

def main():
    print("Welcome to Treasure Hunt! Find all the treasures and avoid the traps!")
    while treasures:
        print_grid()
        move_player()
        if not check_position():
            break
    else:
        print("Congratulations! You found all the treasures! 🏆")

if __name__ == "__main__":
    main()
