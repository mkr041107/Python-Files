import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def write_output_to_file(filename):
    games_played = 0
    highest_losing_streak = 0
    highest_winning_streak = 0
    current_losing_streak = 0
    current_winning_streak = 0
    highest_starting_pennies = 300
    highest_ending_pennies = 0 # Initialize the highest ending pennies
    while True:
        currentbets = 1
        pennies = 300
        output = []
        while pennies >= currentbets:
            coinflip = random.randint(1, 2)
            pennies -= currentbets
            if coinflip == 1:
                currentbets *= 2
                current_winning_streak += 1
                current_losing_streak = 0
            if coinflip == 2:
                pennies += 1
                current_losing_streak += 1
                current_winning_streak = 0
            output.append(f"Bet: {currentbets}, Pennies: {pennies}")
        
        # Update highest streaks if necessary
        if current_losing_streak > highest_losing_streak:
            highest_losing_streak = current_losing_streak
        if current_winning_streak > highest_winning_streak:
            highest_winning_streak = current_winning_streak
        
        # Update highest ending pennies if necessary
        if pennies > highest_ending_pennies:
            highest_ending_pennies = pennies
        
        # Reset current streaks for the next game
        current_losing_streak = 0
        current_winning_streak = 0
        
        with open(filename, 'w') as file:
            for line in output:
                file.write(line + '\n')
        
        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() == 'no':
            break
        games_played += 1
    return games_played, highest_losing_streak, highest_winning_streak, highest_starting_pennies, highest_ending_pennies

def convert_text_to_pdf(text_file, pdf_file, games_played, highest_losing_streak, highest_winning_streak, highest_starting_pennies, highest_ending_pennies):
    c = canvas.Canvas(pdf_file, pagesize=letter)
    y_position = 750 - 50 # Start from the top of the page

    # Set the font to Helvetica-Bold and size to 24 points for the game summary
    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(0, 0, 0) # Set fill color to black for text

    # Game Summary
    game_summary_text = f"Game Summary"
    text_width = c.stringWidth(game_summary_text, "Helvetica-Bold", 24)
    center_x = (letter[0] - text_width) / 2 # Calculate the center position
    c.drawString(center_x, y_position, game_summary_text)
    y_position -= 30 # Move down for the next text

    # Highest Starting Pennies
    text = f"Highest Starting Pennies: {highest_starting_pennies}"
    text_width = c.stringWidth(text, "Helvetica", 6)
    center_x = (letter[0] - text_width) / 2
    c.drawString(center_x, y_position, text)
    y_position -= 30

    # Highest Losing Streak
    text = f"Highest Losing Streak: {highest_losing_streak}"
    text_width = c.stringWidth(text, "Helvetica", 6)
    center_x = (letter[0] - text_width) / 2
    c.drawString(center_x, y_position, text)
    y_position -= 30

    # Highest Winning Streak
    text = f"Highest Winning Streak: {highest_winning_streak}"
    text_width = c.stringWidth(text, "Helvetica", 6)
    center_x = (letter[0] - text_width) / 2
    c.drawString(center_x, y_position, text)
    y_position -= 30

    # Highest Ending Pennies
    text = f"Highest Ending Pennies: {highest_ending_pennies}"
    text_width = c.stringWidth(text, "Helvetica", 6)
    center_x = (letter[0] - text_width) / 2
    c.drawString(center_x, y_position, text)
    y_position -= 30 # Move down for the next text

    # Games Played at the bottom
    games_played_text = f"Games Played: {games_played}"
    text_width = c.stringWidth(games_played_text, "Helvetica", 6)
    center_x = (letter[0] - text_width) / 2
    c.drawString(center_x, y_position, games_played_text)

    c.save()
# Call the function to write output to a file and get the number of games played
games_played, highest_losing_streak, highest_winning_streak, highest_starting_pennies, highest_ending_pennies = write_output_to_file('output.txt')
convert_text_to_pdf('output.txt', 'output.pdf', games_played, highest_losing_streak, highest_winning_streak, highest_starting_pennies, highest_ending_pennies)