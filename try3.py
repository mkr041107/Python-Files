import random
import string

def generate_squares(size=5):
    grid = [['_' for _ in range(size)] for _ in range(size)]
    
    words_to_add = ["able", "back", "calm", "dive", "echo", "firm", "glow", "hunt", "idle", "jump", "kind", "loom", "make", "nest", "open", "pace", "quiz", "rope", "save", "tide", "upon", "vine", "wisp", "xray", "yarn", "zest", "arch", "bold", "chat", "dusk", "ease", "flop", "gaze", "halt", "iced", "jolt", "keep", "lash", "mint", "neon", "oath", "peak", "quip", "rise", "slam", "tame", "undo", "veil", "wolf", "yawn"]
    placed_words = set()

    def place_word(word, orientation, row, col):
        if orientation == 'h':
            if col + len(word) > size:
                return False  # Can't fit horizontally
            grid[row][col:col+len(word)] = word  # Assign the entire word at once
        else:
            if row + len(word) > size:
                return False  # Can't fit vertically
            for i in range(len(word)):
                if row + i >= size:
                    return False  # Out of bounds
                grid[row + i][col] = word[i]
        
        placed_words.add(word)
        return True  # Word was successfully placed

    def check_conflict(word, orientation, row, col):
        if orientation == 'h':
            for i in range(len(word)):
                if col + i >= len(grid[0]) or grid[row][col + i] != '_' and grid[row][col + i] != word[i]:
                    return True
        elif orientation == 'v':
            for i in range(len(word)):
                if row + i >= len(grid) or grid[row + i][col] != '_' and grid[row + i][col] != word[i]:
                    return True
        return False

    placed = 0
    total_words = len(words_to_add)

    for word in words_to_add:
        orientation = random.choice(['h', 'v'])
        
        if orientation == 'h':
            row = random.randint(0, size - 1)
            col = random.randint(0, size - len(word))
        else:
            row = random.randint(0, size - len(word))
            col = random.randint(0, size - 1)

        if check_conflict(word, orientation, row, col):
            continue

        if place_word(word, orientation, row, col):
            placed += 1

    # Fill remaining spaces with random letters
    letters = string.ascii_lowercase
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '_':
                grid[i][j] = random.choice(letters)
    
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def find_words(grid, words):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def search(x, y, word):
        for direction in directions:
            dx, dy = direction
            found_word = ""
            for char in word:
                nx, ny = x + dx * len(found_word), y + dy * len(found_word)
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == char:
                    found_word += char
                else:
                    break
            if found_word == word:
                return True
        return False
    
    found_words = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for word in words:
                if search(x, y, word):
                    found_words.add(word)
    
    return list(found_words)

def main():
    size = 5
    grid = generate_squares(size)
    print_grid(grid)
    
    words_to_find = ["able", "back", "calm", "dive", "echo", "firm", "glow", "hunt", "idle", "jump", "kind", "loom", "make", "nest", "open", "pace", "quiz", "rope", "save", "tide", "upon", "vine", "wisp", "xray", "yarn", "zest", "arch", "bold", "chat", "dusk", "ease", "flop", "gaze", "halt", "iced", "jolt", "keep", "lash", "mint", "neon", "oath", "peak", "quip", "rise", "slam", "tame", "undo", "veil", "wolf", "yawn"]
    found_words = find_words(grid, words_to_find)
    print("\nWords found:", ', '.join(found_words))

if __name__ == "__main__":
    main()

