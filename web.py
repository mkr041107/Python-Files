"""Module to handle web requests."""

import re

import requests
from requests.exceptions import RequestException
from tenacity import retry, stop_after_attempt, wait_fixed
import json


@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def get_letters_from_web():
    try:
        print("Attempting to fetch puzzle config...")
        response = requests.get("https://squaredle.app/api/today-puzzle-config.js")
        puzzle_config = response.text
        print(f"Puzzle config fetched. Length: {len(puzzle_config)}")
        
        # Extract the date from the puzzle config
        date_match = re.search(r'"date":\s*"([^"]+)"', puzzle_config)
        if not date_match:
            print("No date found in puzzle config")
            return set()
        
        date = date_match.group(1)
        print(f"Date extracted: {date}")
        
        # Fetch the puzzle data using the date
        puzzle_url = f"https://squaredle.app/api/puzzle/{date}.js"
        print(f"Fetching puzzle data from: {puzzle_url}")
        puzzle_response = requests.get(puzzle_url)
        
        print(f"Puzzle data status code: {puzzle_response.status_code}")
        print(f"Puzzle data content type: {puzzle_response.headers.get('Content-Type')}")
        
        if puzzle_response.status_code == 200:
            try:
                puzzle_data = puzzle_response.json()
                print(f"Puzzle data fetched. Number of words: {len(puzzle_data['words'])}")
                
                # Extract words from the puzzle data
                words = set(word.lower() for word in puzzle_data['words'])
                print(f"Extracted {len(words)} unique words")
                
                return words
            except json.JSONDecodeError:
                print("Failed to parse JSON response")
                print(f"Response text: {puzzle_response.text[:500]}...")  # Print first 500 characters
                return set()
            else:
                print(f"Failed to fetch puzzle data. Status code: {puzzle_response.status_code}")
                print(f"Response text: {puzzle_response.text[:500]}...")  # Print first 500 characters
                return set()
        
    except RequestException as e:
        print(f"Error fetching letters from web: {e}")
        return set()


def clean_board(raw_board):
    simple = re.sub(r"\n\s+", "", raw_board).strip().replace(" ", "_")
    return re.sub(r'[",]', "", simple)


def get_latest_puzzle_date(puzzle_config):
    if date_match := re.search(r'"date":\s*"([^"]+)"', puzzle_config):
        return date_match.group(1)
    return "Unknown"

def generate_squaredle(size=5):
    grid = [['_' for _ in range(size)] for _ in range(size)]
    
    print("Fetching words from web...")
    words_to_add = list(get_letters_from_web())[:10]  # Get the first 10 words from the web
    print(f"Fetched {len(words_to_add)} words from web.")
    print(f"Words fetched: {words_to_add}")
    
