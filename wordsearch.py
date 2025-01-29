import random
import string

def generate_word_search(max_rows=15, max_cols=None, max_words=10, max_attempts=100):
    if max_cols is None:
        max_cols = int(max_rows * 0.7)  # Make it approximately 70% as wide as tall
    
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)

    word_list = [
        "AUTRE", "PPLEF", "TIGER", "EAGLE", "RANGE",
        "TEAR", "PEAL", "TARE", "REAP", "PEAT",
        "BRAIN", "SPACE", "TIME", "MIND", "HEART",
        "SOUL", "BODY", "HAND", "FOOT", "HEAD",
        "EAR", "EYE", "NOSE", "MOUTH", "TOOTH",
        "SKULL", "NECK", "BACK", "ARM", "LEG",
        "KNEE", "ELBOW", "SHOULDER", "HIP", "ANKLE",
        "TOES", "FINGERS", "WINGS", "ROOTS", "SEEDS",
        "FLOWER", "TREE", "GRASS", "ROCK", "MOUNTAIN",
        "VALLEY", "RIVER", "OCEAN", "SKY", "CLOUD",
        "RAIN", "SNOW", "SUN", "MOON", "STAR",
        "PLANET", "GALAXY", "UNIVERSE", "ATOM", "MATTER",
        "ENERGY", "FORCE", "POWER", "LIGHT", "SOUND",
        "COLOR", "SHAPE", "SIZE", "WEIGHT", "TEMPERATURE",
        "PRESSURE", "VOLUME", "TIME", "AGE", "DATE",
        "YEAR", "MONTH", "DAY", "WEEK", "QUARTER",
        "HALF", "FULL", "EMPTY", "OPEN", "CLOSED",
        "FAST", "SLOW", "BIG", "SMALL", "OLD", "NEW",
        "HOT", "COLD", "WET", "DRY", "CLEAN", "DIRTY",
        "NICE", "BAD", "GOOD", "RIGHT", "WRONG"
    ]

    filtered_word_list = [word for word in word_list if len(word) <= min(max_rows, max_cols) // 2]

    grid = [['_' for _ in range(max_cols)] for _ in range(max_rows)]
    placed_words = []

    def place_word(word):
        direction = random.choice(['across', 'down'])
        
        if direction == 'across':
            row = random.randint(0, max_rows - 1)
            col = random.randint(0, max_cols - len(word))
            
            if col < 0:
                return False
            
            for i, letter in enumerate(word):
                grid[row][col + i] = letter
        else:
            row = random.randint(0, max_rows - len(word))
            col = random.randint(0, max_cols - 1)
            
            if row < 0:
                return False
            
            for i, letter in enumerate(word):
                grid[row + i][col] = letter
        return True

    def place_word_with_attempts(word, max_attempts):
        attempts = 0
        while attempts < max_attempts:
            if place_word(word):
                return True
            attempts += 1
        return False

    placed_words = []
    for word in filtered_word_list[:]:
        if place_word_with_attempts(word, max_attempts):
            placed_words.append(word)
        else:
            print(f"Skipping {word} due to max attempts reached")

    for row in range(max_rows):
        for col in range(max_cols):
            if grid[row][col] == '_':
                grid[row][col] = random.choice(alphabet)

    return grid, placed_words

def play_game():
    size = 15
    max_attempts = 100
    grid, words_to_find = generate_word_search(size, max_words=10, max_attempts=max_attempts)
    
    print("Welcome to Word Search!")
    print("Guess words by typing them. Type 'quit' to end the game.")
    
    while True:
        print_grid(grid)
def print_grid(grid):
    print("\nWord Search Puzzle:")
    for row in grid:
        print(' '.join(row))
        
        guess = input("Your guess: ").strip().upper()
        if guess == "DEBUG":
            print(words_to_find)
        if guess == 'QUIT':
            break
        
        if len(guess) > size:
            print("Please guess a word shorter than or equal to the grid size.")
            continue
        
        # Check all possible orientations for the word
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # across, down, diagonal, anti-diagonal
        
        found_in_grid = False
        for direction in directions:
            row_offset, col_offset = direction
            
            # Check all possible starting positions
            for start_row in range(size):
                for start_col in range(size - len(guess) + 1):
                    word_found = True
                    
                    for i, letter in enumerate(guess):
                        grid_row = start_row + i * row_offset
                        grid_col = start_col + i * col_offset
                        
                        # Check if the letter is within the grid boundaries
                        if (0 <= grid_row < size) and (0 <= grid_col < size):
                            if grid[grid_row][grid_col] != letter:
                                word_found = False
                                break
                    
                    if word_found:
                        found_in_grid = True
                        break
        
        if found_in_grid:
            if guess in words_to_find:
                words_to_find.remove(guess)
                print("Correct!!")
                
                if not words_to_find:
                    print("Congratulations! You've found all the words!")
                    break
            else:
                print("Word not found in the list.")
        else:
            print("Word not found in the grid.")

if __name__ == "__main__":
    play_game()
