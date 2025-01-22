import random
import string

def generate_squares(size=5):
    grid = [['_' for _ in range(size)] for _ in range(size)]
    
    words_to_add = ["able", "back", "calm", "dive", "echo"]
    for word in words_to_add:
        orientation = random.choice(['h', 'v'])
        placed = False
        
        while not placed:
            if orientation == 'h':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - len(word))
                
                # Check if the word can be placed without conflicts
                conflict = False
                for i in range(len(word)):
                    if grid[row][col + i] != '_' and grid[row][col + i] != word[i]:
                        conflict = True
                        break
                
                if not conflict:
                    for i in range(len(word)):
                        grid[row][col + i] = word[i]
                    placed = True
    
            else:
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - 1)
                
                # Check if the word can be placed without conflicts
                conflict = False
                for i in range(len(word)):
                    if grid[row + i][col] != '_' and grid[row + i][col] != word[i]:
                        conflict = True
                        break
                
                if not conflict:
                    for i in range(len(word)):
                        grid[row + i][col] = word[i]
                    placed = True
    
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
    size = 7  # Increased size to accommodate more words
    grid = generate_squares(size)
    print_grid(grid)
    
    words_to_find = ["able", "back", "calm", "dive", "echo"]
    found_words = find_words(grid, words_to_find)
    print("\nWords found:", ', '.join(found_words))

if __name__ == "__main__":
    main()

