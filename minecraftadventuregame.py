import random

# Define your entities here
player_x = 4 # Initial position of the player
player_y = 4 # Initial position of the player
monster = [7, 3, 0, 0] # Example coordinates and velocity for monster
#enemy = [2, 8, 0, 0] # Example coordinates and velocity for enemy
letters = [monster] # Start with the player
monstercount =1


# The rest of your game code, including the game_loop function
world = [
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
]

# Place the player in the middle of the world
world[4][4] = 'P'

# Function to generate unique coordinates and place an entity in the world
def generate_unique_coordinates_and_place_entity(world, entity_char):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        # Check if the new coordinates are not already occupied in the world
        if world[y][x] == ' ':
            world[y][x] = entity_char
            return x, y

# Generate unique coordinates for multiple entities
entities = ['M'] # Example: Monster, Player, Enemy
for entity_char in entities:
    x, y = generate_unique_coordinates_and_place_entity(world, entity_char)
    print(f"{entity_char} coordinates: ({x}, {y})")

# Generate unique coordinates for the winning location
rndxposwin, rndyposwin = generate_unique_coordinates_and_place_entity(world, 'W') # 'W' for Winning location

def print_world(world):
    for row in world:
        for cell in row:
            # Check if the cell is a monster or the winning position
            # Assuming 'M' represents a monster and 'W' represents the winning position
            if cell == 'M' or cell == 'W':
                # Skip printing these cells
                continue
            print(cell, end=' ')
        print() # Print a newline after each row

def move_player(command, world):
    global player_x, player_y # Declare player_x and player_y as global
    world[player_y][player_x] = ' '
    
    # Update the player's position based on the direction
    if command == 'up' and player_y > 1:
        player_y -= 1
    elif command == 'down' and player_y < 9:
        player_y += 1
    elif command == 'left' and player_x > 1:
        player_x -= 1
    elif command == 'right' and player_x < 8:
        player_x += 1
    else:
        print("You can't move that way.")
        print("You are at ({}, {})".format(player_x, player_y))
    
    world[player_y][player_x] = 'P'
    return int(player_x), int(player_y)
def find_entities(world):
    entities = {'M': 'Monster', 'E': 'Enemy'} # Dictionary to map entity characters to their names
    entity_positions = {name: [] for name in entities.values()} # Initialize an empty list for each entity

    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            if cell in entities:
                entity_positions[entities[cell]].append((x, y))

    return entity_positions

def reset_game():
    global world, player_x, player_y, rndxposwin, rndyposwin, monstercount, letters
    world = [
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '~'],
        ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
    ]
    
    rndxposwin, rndyposwin = generate_unique_coordinates_and_place_entity(world, 'W') # 'W' for Winning location
    monstercount =+ 1 # Reset the monster count
    letters = [generate_unique_coordinates_and_place_entity(world, 'M') for _ in range(monstercount)]
    player_x, player_y = 4, 4
    world[4][4] = 'P'
    world[rndyposwin][rndxposwin] = 'W'
def game_loop():
    global world # Declare world as global
    global player_x, player_y # Declare player_x and player_y as global
    global rndxposwin, rndyposwin
    global letters
    global monstercount
    game_over = False
    while not game_over: # Check the flag in the outer loop condition
        print_world(world)
        print("Player position:", (player_x, player_y))
        print("Enter a direction to move: up, down, left, right, or quit")

        command = input().lower()

        if command == 'quit':
            game_over = True # Set the flag to True to exit the game
            break

        # Check for monsters before moving the player
        entity_positions = find_entities(world)
        monster_positions = entity_positions.get('Monster', [])
        if (player_y, player_x) in monster_positions:
            print("Helllo")
            # Handle monster encounter logic here
            pass

        # Now move the player
        move_player(command, world)

        # Check for winning condition after each move
        if rndxposwin == player_x and rndyposwin == player_y:
            print("You Win!!")
            play_again = input("Play Again? y/n: ").lower()
            if play_again == 'n':
                game_over = True # Set the flag to True to exit the game
                break
            else:
                reset_game()
                
        if (player_x, player_y) in monster_positions:
            print ("Helllo")
            monstertype= random.randint(0,1)
            while True:
                if monstertype == 1:
                    print("OH NO! You found a creeper!!")
                    fleeorfight = input("Do you flee or fight?")
                    if fleeorfight == 'flee':
                        fleechance = random.randint(0,1)
                        if fleechance == 0:
                            print("You Got Blown To Smithereens")
                            play_again = input("Play Again? y/n: ").lower()
                            if play_again == 'n':
                                game_over = True # Set the flag to True to exit the game
                                break
                            else:
                                reset_game()
                                break
                        else:
                            print("you survived the cointoss of fate")
                            break
                    if fleeorfight == 'fight':
                        fight2 = random.randint(0,1)
                        if fight2 == 0:
                            print("You absolute buffoon, how did you not see the creeper was about to blow up. Now you exploded and your guts poured to the ground")
                            play_again = input("Play Again? y/n: ").lower()
                            if play_again == 'n':
                                game_over = True # Set the flag to True to exit the game
                                break
                            else:
                                reset_game()
                                break
                        if fight2 == 1:
                            print("You lucky person you grabbed tyhe wrong set of armor instead of the protection you grabbed blast protection you survived!")
                            break
                    else:
                        print("Try again")
                        break
                if monstertype == 0:
                    print("OH NO its a zombie")
                    fleeorfight2 = input("Do you flee or fight?")
                    if fleeorfight2 == 'flee':
                        fleechance2 = random.randint(0,3)
                        if fleechance2 <= 2:
                            print ("You Ran Away Succesfully!! Those Slow Zombies!! ")
                            break
                        else:
                            print("you managed to get killed by that slow zombie! you bumbling idiot!!")
                            play_again = input("Play Again? y/n: ").lower()
                            if play_again == 'n':
                                break
                            else:
                                reset_game()
                                break
                    if fleeorfight2 == 'fight':
                        fight = random.randint(0,1)
                        if fight == 0:
                            print("you idiot you forgot your diamond armor at your house, too bad you dont respawn LOL¯\_(ツ)_/¯")
                            play_again = input("Play Again? y/n: ").lower()
                            if play_again == 'n':
                                game_over = True # Set the flag to True to exit the game
                                break
                            else:
                                reset_game()
                                break
                        if fight == 1:
                            print("You sucessfully remebered to bring your diamond gear, you kill the zombie")
                            break
                    else:
                        print("Try again")
                        break
            pass

if __name__ == "__main__":
    game_loop()

