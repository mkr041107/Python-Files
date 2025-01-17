import random

word_list = ["abandon", "ability", "absence", "academy", "account", "accused", "achieve", "acquire", "address", "advance",
"adverse", "advised", "adviser", "against", "airline", "airport", "alcohol", "alleged", "already", "analyst",
"ancient", "another", "anxiety", "anxious", "anybody", "applied", "arrange", "arrival", "article", "assault",
"assumed", "assured", "attempt", "attract", "auction", "average", "backing", "balance", "banking", "barrier",
"battery", "bearing", "beating", "because", "bedroom", "believe", "beneath", "benefit", "besides", "between",
"billion", "binding", "brother", "brought", "burning", "cabinet", "caliber", "calling", "capable", "capital",
"captain", "caption", "capture", "careful", "carrier", "caution", "ceiling", "central", "centric", "century",
"certain", "chamber", "channel", "chapter", "charity", "charlie", "charter", "checked", "chicken", "chronic",
"circuit", "classes", "classic", "climate", "closing", "closure", "clothes", "collect", "college", "combine",
"comfort", "command", "comment", "compact", "company", "compare", "compete", "complex", "concept", "concern",
"concert", "conduct", "confirm", "connect", "consent", "consist", "contact", "contain", "content", "contest",
"context", "control", "convert", "correct", "council", "counsel", "counter", "country", "crucial", "crystal",
"culture", "current", "cutting", "dealing", "decided", "decline", "default", "defence", "deficit", "deliver",
"demand", "denying", "depart", "depend", "deposit", "depth", "deputy", "deserve", "design", "desire", "detail",
"detect", "develop", "device", "devote", "differ", "dinner", "direct", "discuss", "disease", "display", "dispute",
"distance", "diverse", "divided", "drawing", "driving", "dynamic", "eastern", "economy", "edition", "elderly",
"element", "engaged", "enhance", "enquiry", "episode", "equally", "essence", "evening", "evident", "exactly",
"examine", "example", "exceed", "exclude", "excuse", "execute", "exhibit", "expense", "explain", "explore",
"express", "extreme", "factory", "faculty", "failing", "failure", "fashion", "feature", "federal", "feeling",
"fiction", "fifteen", "filling", "finance", "finding", "fishing", "fitness", "foreign", "forever", "formula",
"fortune", "forward", "founder", "freedom", "further", "gallery", "gateway", "general", "genetic", "genuine",
"gesture", "getting", "giveaway", "glimpse", "greater", "hanging", "heading", "healthy", "hearing", "heavily",
"helpful", "helping", "herself", "highway", "himself", "history", "holding", "holiday", "housing", "however",
"hundred", "husband", "illegal", "illness", "imagine", "imaging", "improve", "include", "initial", "inquiry",
"insight", "install", "instant", "instead", "intense", "interim", "involve", "jointly", "journal", "journey",
"justice", "justify", "keeping", "killing", "kingdom", "kitchen", "knowing", "landing", "largely", "lasting",
"leading", "learned", "leisure", "liberal", "liberty", "library", "license", "limited", "listing", "logical",
"loyalty", "machine", "manager", "mansion", "marginal", "married", "massive", "maximum", "meaning", "measure",
"medical", "meeting", "mention", "message", "million", "mineral", "minimal", "minimum", "missing", "mission",
"mistake", "mixture", "monitor", "monthly", "morning", "musical", "mystery", "natural", "neither", "nervous",
"network", "neutral", "notable", "nothing", "nowhere", "nuclear", "nursing", "obvious", "offense", "officer",
"ongoing", "opening", "operate", "opinion", "optical", "organic", "outcome", "outdoor", "outlook", "outside",
"overall", "pacific", "package", "painted", "parking", "partial", "partner", "passage", "passing", "passion",
"passive", "patient", "pattern", "payable", "payment", "penalty", "pending", "pension", "percent", "perfect",
"perform", "perhaps", "phoenix", "picking", "picture", "pioneer", "plastic", "platform", "playing", "pleased",
"pleasure", "plenty", "pocket", "popular", "portion", "poverty", "precise", "predict", "premier", "premium",
"prepare", "present", "prevent", "primary", "printer", "privacy", "private", "problem", "proceed", "process",
"produce", "product", "profile", "program", "project", "promise", "promote", "protect", "protein", "protest",
"provide", "publish", "purpose", "pursuit", "qualify", "quality", "quarter", "radical", "railway", "readily",
"reading", "reality", "realize", "receipt", "receive", "recover", "reflect", "reform", "refugee", "regard",
"regular", "related", "release", "remains", "removal", "removed", "replace", "request", "require", "reserve",
"resolve", "respect", "respond", "restore", "retired", "revenue", "reverse", "rollout", "routine", "running",
"satisfy", "science", "section", "segment", "serious", "service","service", "shadow", "shaped", "shift", "short", "shown", "signal", "simple", "since", "sister", "slight", "small", 
"smart", "smoke", "smooth", "social", "soldier", "source", "special", "speech", "spend", "spirit", "spread", "spring", 
"stable", "stand", "start", "state", "steady", "steel", "step", "still", "stomach", "stone", "story", "stream", 
"street", "stress", "strike", "strong", "student", "study", "style", "submit", "success", "suggest", "summer", "supply", 
"support", "surface", "survive", "switch", "symbol", "system", "table", "tackle", "talent", "target", "teaching", 
"technology", "tension", "testing", "theory", "therapy", "thinking", "threat", "through", "tobacco", "together", 
"tomorrow", "tourism", "traffic", "training", "transfer", "travel", "treaty", "trouble", "universe", "upgrade", 
"upward", "utility", "vacancy", "variety", "vehicle", "venture", "victory", "village", "virtual", "visible", 
"visitor", "vitamin", "voltage", "volunteer", "warning", "welfare", "western", "whisper", "widely", "window", 
"witness", "wonder", "working", "writing", "yawning", "yearly", "yielding", "yogurt", "younger", "zebra", 
"zephyr", "zigzag", "zodiac", "zombie", "zone", "zoom"]

word_list = [word.strip().lower() for word in word_list if word.strip()]
random.shuffle(word_list)

def generate_grid(word_list, grid_size=5):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    

    def place_word(grid, word, direction):
        rows, cols = len(grid), len(grid[0])
        start_x, start_y = random.randint(0, rows - 1), random.randint(0, cols - 1)
    
        for i in range(len(word)):
            new_x, new_y = start_x + direction[0] * i, start_y + direction[1] * i
            
            if 0 <= new_x < rows and 0 <= new_y < cols:
                grid[new_x][new_y] = word[i]
            else:
           
                return False
        
        return True

    def find_best_direction(grid, word):
        best_score = float('-inf')
        best_direction = None
        
        for direction in directions:
            score = 0
            
            for i in range(len(word)):
                new_x, new_y = grid_size // 2 + direction[0] * i, grid_size // 2 + direction[1] * i
                
                if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
                    score += 1
                else:
                    break
            
            if score > best_score:
                best_score = score
                best_direction = direction
        
        return best_direction

    def place_words(grid, word_list):
        random.shuffle(word_list)
        
        for word in word_list:
            best_direction = find_best_direction(grid, word)
            
            if place_word(grid, word, best_direction):
                return True
        
        return False

    # Main grid generation loop
    while len(word_list) > 0:
        if not place_words(grid, word_list[:]):
            break
    
    
        return True



    
    # Place words in the grid
    for word in word_list:
        placed = False
        attempts = 0

        while not placed and attempts < max_attempts:
            # Try all directions
            for direction in directions:
             if all(letter not in used_letters for letter in word):
                if place_word_from_center(grid, word, direction):
                    placed = True

                    # Update used letters only after successful placement
                    
                    used_letters.update(word)
                    attempts = 0
                    break  # Exit the inner loop once word is placed
                else:
                    attempts += 1
            else:
                # If we've tried all directions without placing the word
                attempts += 1

        if not placed:
            print(f"Warning: Could not place '{word}' after {max_attempts} attempts")

    return grid

# Function to display the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    
    print(f"Remaining letters: {set('abcdefghijklmnopqrstuvwxyz') - set(cell for row in grid for cell in row)}")

# Generate and print the grid
grid = generate_grid(word_list)
print_grid(grid)
