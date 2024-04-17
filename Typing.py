import time
import random
from pynput import keyboard

file_path = r'H:\PI\helllllllllllllllo.txt'
wpm_path = r'H:\PI\wpm.txt'

highest_wpm = 0

def get_sentence():
    with open(file_path, 'r') as file:
        return random.choice(file.read().split(".")).strip()

def count_lines_in_file(file_path):
    with open(file_path, 'r') as fp:
        return sum(1 for line in fp if line.strip())

def update_highest_wpm(wpm):
    global highest_wpm
    with open(wpm_path, 'r') as wpm_file:
        highest_wpm_in_file = max(int(line) for line in wpm_file if line.strip().isdigit())
    if wpm > highest_wpm_in_file:
        highest_wpm = wpm
        with open(wpm_path, 'a') as wpm_file:
            wpm_file.write(f"{round(wpm)}\n")
        print("Highest WPM updated.")
    else:
        print("Highest WPM not updated.")

def start_typing_test():
    global highest_wpm # Declare highest_wpm as a global variable
    ssssentence = get_sentence()
    print(f"Type the following sentence: {ssssentence}")
    accuracy_count = 0



    with keyboard.Events() as events:
        stassstime = time.time()
        typssssentence = input("Type the sentence: ")
        wpm = (len(ssssentence.split()) / (time.time() - stassstime)) * 60

        for i in range(min(len(ssssentence), len(typssssentence))):
            if ssssentence[i] == typssssentence[i]:
                accuracy_count += 1
        accuracy = (accuracy_count / len(ssssentence)) * 100 if ssssentence else 0

    print(f"Your WPM is: {round(wpm)}")
    print(f"Accuracy: {accuracy:.2f}%")

    update_highest_wpm(wpm)

    num_tests = count_lines_in_file(wpm_path)
    if num_tests > 0:
        with open(wpm_path, 'r') as wpm_file:
            total_wpm = sum(int(line) for line in wpm_file if line.strip().isdigit())
        average_wpm = total_wpm / num_tests
        print(f"Average WPM: {round(average_wpm)}")
        print(f"Highest WPM: {round(highest_wpm)}")
    else:
        print("No tests were taken.")

    if typssssentence.strip() == ssssentence:
        print("You got it right!")
        return True
    else:
        print("You got it wrong. Try again.")
        return False

while True:
    if start_typing_test():
        print("Do you want to try again? (yes/no)")
        response = input().lower()
        if response != 'yes':
            break
    else:
        print("Do you want to try again? (yes/no)")
        response = input().lower()
        if response != 'yes':
            break
