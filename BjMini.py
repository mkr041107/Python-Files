import random

money = 500


bets = 0
bets = int(input("How Much Do You Want To Bet:"))

while money >= bets:
    DealerCard = random.randint(2,14)
    UserCard = random.randint(2,14)
    if DealerCard == 11:
            print("Jack")
    elif DealerCard ==12:
            print("Queen")
    elif DealerCard == 13:
            print ("King")
    elif DealerCard == 14:
            print("Ace")
    else:
            print(f"Dealer: {DealerCard}")
    if UserCard == 11:
            print("Jack")
    elif UserCard ==12:
            print("Queen")
    elif UserCard == 13:
            print ("King")
    elif UserCard == 14:
        print("Ace")
    else:
            print(f"User: {UserCard}")
    if DealerCard > UserCard:
        currentbet = 0
        currentbet += bets*2
        bets= currentbet
        print(f"Current Bet: {currentbet}")
        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() == 'no':
            break
    else: 
        currentbet = bets
        print(f"Current Bet: {currentbet}")
        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() == 'no':
            break