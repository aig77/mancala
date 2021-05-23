from Minimax import Minimax
from MancalaAction import MancalaAction
from MancalaState import MancalaState

if __name__ == '__main__':

    depth = 3
    print('How many pits on each side?')
    pits = (int)(input())
    print('How many stones per pit to begin with?')
    stones = (int)(input())
    print("Who should start? 1=you 2=computer ")
    player =(int)(input())
    while player < 1 or player > 2:
        print('invalid input. try again')
        player =(int)(input())

    s = MancalaState(pits, stones)
    s.player = player

    print('The game will be displayed like this \n')
    s.printstate()
    print('where the bottom row represents the player that is goes first with their mancala to the right')
    print('and the top row represents the player that goes second with their mancala to the left')
    print('meaning the game moves in a counterclock wise fashion.')
    print('\n')

    pit_str = f'(0-{pits-1})' if player == 1 else f'({pits+1}-{pits*2})'

    while(1):
        if s.playerToMove != player:
            print('CPU move!')
            minimax = Minimax(depth)
            s = s.getResult(minimax.MinimaxDecision(s))
        else:
            print('Your move!')
            print('Pick a pit', pit_str)
            while(1):
                temp = (int)(input())
                if temp in (action.getPit() for action in s.getActions()):
                    break
                print('Invalid entry. Try again')
            a = MancalaAction(player, temp)
            s = s.getResult(a)
        s.printstate()
        if s.isTerminal():
            break
    if(s.getUtility() > 0):
        print('You lost')
    elif(s.getUtility() < 0):
        print('You win')
    else:
        print('Draw')
