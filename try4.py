import random
import string

def generate_squares(size=5):
    grid = [['_' for _ in range(size)] for _ in range(size)]
    
    words_to_add = [
        ["NO", "ON"],
        ["DE", "ED"],
        ["CI", "VI"],
        ["MA", "DA"],
        ["RA", "DA"],
        ["AB", "LE"],
        ["BA", "CK"],
        ["CA", "LM"],
        ["DI", "VE"],
        ["EC", "HO"]

    ]

    
    if __name__ == "__main__":
        main()

    placed = 0
    total_words = len(words_to_add)

    for word_pair in words_to_add:
        orientation = random.choice(['square', 'diagonal'])
        success = False
        
        for _ in range(100):  # Try 100 times to place the word
                row = random.randint(0, size - len(word))
                success = True
                break
        
        if not success:
            break
            print(f"Warning: Could not place '{word}'")

    # Fill remaining spaces with random letters
    letters = string.ascii_lowercase
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '_':
                grid[i][j] = random.choice(letters)
    
    return grid, words_to_add

def find_words(grid, words):

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def search(x, y, word):
        for dx, dy in directions:
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

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def place_words(grid, words_to_add):
    size = len(grid)
    
    def place_word(word, orientation, row, col):
        if orientation == 'square':
            if row + len(word) > size or col + len(word) > size:
                return False  # Can't fit in square
            for i in range(len(word)):
                grid[row + i][col + i] = word[i]
            return True  # Word was successfully placed
        
        elif orientation == 'diagonal':
            if row + len(word) > size or col + len(word) > size:
                return False  # Can't fit diagonally
            for i in range(len(word)):
                if grid[row + i][col + i] != '_' and grid[row + i][col + i] != word[i]:
                    return False
            for i in range(len(word)):
                grid[row + i][col + i] = word[i]
            return True  # Word was successfully placed
        
        elif orientation == 'stacked':
            if row + len(word) > size or col + len(word) > size:
                return False  # Can't fit stacked
            for i in range(len(word)):
                grid[row][col + i] = word[i]
            return True  # Word was successfully placed
    
    placed_words = set()
    total_words = len(words_to_add)
    
    for word_pair in words_to_add:
        success = False
        
        for _ in range(100):  # Try 100 times to place the word
            row = random.randint(0, size - len(word_pair[0]))
            col = random.randint(0, size - len(word_pair[1]))
            
            if place_word(word_pair[0], 'stacked', row, col):
                success = True
                break
            
            if place_word(word_pair[1], 'stacked', row, col):
                success = True
                break
        
        if not success:
            print(f"Warning: Could not place '{word_pair[0]}{word_pair[1]}'")
    
    return grid, words_to_add

def main():
    size = 5
    grid, words_to_add = generate_squares(size)
    print_grid(grid)
    
    found_words = find_words(grid, words_to_add)
    print("\nWords found:", ', '.join(found_words))

if __name__ == "__main__":
    main()
