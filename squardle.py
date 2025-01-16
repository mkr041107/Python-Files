import random

# Function to generate a random number between 1 and 26
def random_alphabetic_number():
    return random.randint(1, 26)
# Initialize the 5x5 grid with random numbers between 1 and 26
word_list=["abandon", "ability", "absence", "academy", "account", "accused", "achieve", "acquire", "address", "advance",
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
"zephyr", "zigzag", "zodiac", "zombie", "zone", "zoom"
]
grid = [[random_alphabetic_number() for _ in range(5)] for _ in range(5)]
# Print the grid
for row in grid:
    print(row)
    
def number_to_letter(number):
    return chr(ord('a')+number - 1)
grid_letters = {number_to_letter(num) for row in grid for num in row}

# Output the filtered words
# Accessing individual elements
#print("\nAccessing elements:")
#print(f"Element at (0,0): {grid[0][0]}")
#print(f"Element at (2,3): {grid[2][3]}")

# Modifying elements
#print("\nModifying elements:")
#grid[1][1] = random_alphabetic_number()
#print(f"After modifying: {grid[1][1]}")

for row in grid:
    print(' '.join(number_to_letter(num)for num in row))  # 1
filtered_words = [
    word for word in word_list 
    if len(word) >= 4 and all(char in grid_letters for char in word)
]

print(filtered_words)
    
guess = input()
