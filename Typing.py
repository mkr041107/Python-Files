import time
import random

# Corrected file path
file_path = r'H:\PI\hellllllllllllllloo.txt'

# Read the file and split it into sentences
with open(file_path, 'r') as file:
    sentences = file.read().split(".")

ssssentence = random.choice(sentences).strip()

print(f"Type the following sentence: {ssssentence}")

stassstime = time.time()
typssssentence = input("Type the sentence: ")
endsstime = time.time()
elapsedeeetime = endsstime - stassstime


wordseeinssentence = len(ssssentence.split())
wpm = (wordseeinssentence / elapsedeeetime) * 60


if typssssentence.strip() == ssssentence:
    print(f"Your WPM is: {wpm}")
else:
    print("You got it wrong. Try again.")