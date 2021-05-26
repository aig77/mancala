from Minimax import Minimax
from MancalaAction import MancalaAction
from MancalaState import MancalaState

if __name__ == '__main__':

    depth = 30
    print('How many pits on each side?')
    pits = (int)(input())
    print('How many stones per pit to begin with?')
    stones = (int)(input())
    print("Who should start? 1=you 2=computer ")
    player =(int)(input())
    while player != 1 and player != 2:
        print('invalid input. try again')
        player =(int)(input())

    s = MancalaState(pits, stones)
    s.playerToMove = player

    print('The game will be displayed like this \n')
    s.printstate()
    print('\nwhere the bottom row represents the player with their mancala to the right')
    print('and the top row represents the computer with their mancala to the left')
    print('meaning the game moves in a counterclock wise fashion.')
    print('\n')

    pit_str = f'(0-{pits-1})'
    move_count = 1

    while(1):
        print('Move', str(move_count))
        # player turn
        if s.playerToMove == 1:
            print('Your move!')
            print('Pick a pit', pit_str)
            while(1):
                temp = (int)(input())
                if temp in (action.getPit() for action in s.getActions()):
                    break
                print('Invalid entry. Try again')
            a = MancalaAction(s.playerToMove, temp)
            s = s.getResult(a)
        # computer turn
        else:
            print('CPU move!')
            minimax = Minimax(depth)
            s = s.getResult(minimax.minimaxDecision(s))
        s.printstate()
        print('----------------------------')
        move_count+=1
        if s.isTerminal():
            s.clearGame()
            s.updateUtility()
            print('Game over. Clearing board...')
            s.printstate()
            break
    if(s.getUtility() > 0):
        print('You win')
    elif(s.getUtility() < 0):
        print('You lose')
    else:
        print('Draw')
