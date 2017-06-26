def start():
    print ('Instructions for Rock, Paper, Scissors, Lizard, Spock:'
        ' '
    'This game is a remix of Rock, Paper, Scissors.' ' '
    'Each player picks a variable and reveals it at the same time.' ' '
    'The winner is the one who defeats the others. In a tie, the process is repeated until a winner is found.' ' '
    'Scissors cuts Paper,''/n'+
    'Paper covers Rock,''/n'
    'Rock crushes Lizard,''/n'
    'Lizard poisons Spock,''/n'
    'Spock smashes Scissors,''/n'
    'Scissors decapitates Lizard,''/n'
    'Lizard eats Paper,''/n'
    'Paper disproves Spock,''/n'
    'Spock vaporizes Rock,''/n'
    'Rock crushes Scissors''/n')
    
    
    
    user1 = raw_input('What is your name?')
    user2 = raw_input('And your name?')
    print ("\n")
    print (user1+' Begin play')
    user1_answer = raw_input(user1+' ''do you want to choose rock, paper, scissors, lizard, or Spock? ')
    print ('\f')
    print ('\f')
    print (user2+' it is your turn.')
    user2_answer = raw_input(user2+' ' 'do you want to choose rock, paper, scissors, lizard, or Spock? ')
    compare(user1_answer, user2_answer)
    

def compare(u1, u2):
    if u1 == u2:
        print("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'Spock':#Spock and Paper beats Rock
            print("Spock wins!")
        elif u2 == 'paper':
            print("Paper wins!")    
        else:
            print("Rock wins!")
    elif u1 == 'scissors':
        if u2 == 'rock':#Rock and Spock beats Scissors
            print("Rock wins!")
        elif u2 == 'Spock':
            print("Spock wins!")
        else:
            print("Scissor wins!")
    elif u1 == 'paper':
        if u2 == 'lizard':#Lizard and Scissors beats Paper
            print("Lizard wins!")
        elif u2 == 'scissors':
            print("Scissor wins!")
        else:
            print("Paper wins!")
    elif u1 == 'lizard':
        if u2 == 'rock':#Rock and Scissors beat Lizard
            print("Rock wins!")
        elif u2 == 'scissors':
            print("Scissors win!")
        else:
            print("Lizard wins!")
    elif u1 == 'Spock':
        if u2 == 'lizard':#Lizard and Paper beat Spock
            print("Lizard wins!")
        elif u2 == 'paper':
            print("Paper wins!")
        else:
            print("Spock wins!")   
    else:  
        print("Invalid input! You have not entered rock, paper, scissors,lizard, or Spock (case sensitive) try again.")
        
start()