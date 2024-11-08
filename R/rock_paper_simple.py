# return the winner of rock paper scissors

def rock_paper_scissors(p1,p2):
    winner = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if p1 == p2:
        return "Draw!"
    elif winner[p1] == p2:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"