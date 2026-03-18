#  making a little progarm about rock paper scissors

import random

options=['rock','paper','scissor']

running=True

while running:
    
    
    player=None
    compyuter=random.choice(options)
    
    while player not in options:
        
        player=input("Enter your choice(rock paper,scissor): ")

    print(f'AI: {compyuter}')
    print(f'Player: {player}')

    if compyuter==player:
        print('It`s a tie')
    elif compyuter=='scissor' and player=='rock':
        print('you win')
    elif compyuter=='rock' and player=='paper':
        print('you win')
    elif compyuter=='paper' and player=='scissor':
        print('you win')
    else:
        print('you lose! AI win')   
    
    # play_again=input("play again(y/n): ").lower()
    # if not play_again=='y':
    #     running=False
    if not input("play again? (y.n): ").lower() =='y':
        running=False
        
print("Game stopped! thanks for playing!")
