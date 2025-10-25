def determine_winner(player1, player2):
    winning_comb = {("rock","scissor"): "player 1", ("paper,rock"):"player 2", ("scissors","paper"):"player 1",("scissors","rock"):"player 2",("rock", "paper"):"Player 2",
        ("paper","scissors"): "Player 2",("rock", "rock"):"Tie",("paper","paper"):"Tie",("scissors","scissors"): "Tie"}
    return winning_comb.get((player1, player2),"Invalid")

player1_choice = input("Player 1 , enter your choice (rock/paper/scissors): ").lower()
player2_choice = input("Player 2 , enter your choice (rock/paper/scissors): ").lower()

result = determine_winner(player1_choice, player2_choice)
if result == 'Player 1':
    print("Player 1 is  winner!!")
elif result == 'Player 2':
    print("Player 2 is winner!!")
else:
    print("It's a tie!!")    

