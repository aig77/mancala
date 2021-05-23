from MancalaAction import MancalaAction

class MancalaState:

    def __init__(self, pits=3, stones=3):
        # boards portray the current position of the game
        # the numbers represent the number of beads in each player's hole
        self.board = self.initBoard(pits, stones)
        self.mancala1 = pits
        self.mancala2 = pits*2 + 1
        self.player = 1 # the player either 1 or 2
        self.playerToMove = 1 # the player that is about to move
        self.utility = 0 # utiltiy value of the state.
        self.moves = 0 # number of moves played 

    def initBoard(self, pits, stones):
        board = []
        for i in range(2):
            for j in range(pits):
                board.append(stones)
            board.append(0)
        return board

    def updateUtility(self):
        u = self.board[self.mancala1] - self.board[self.mancala2]
        self.utility = u if self.player == 2 else u * -1

    def getActions(self):
        # For Mancala, each player has one valid action for every non
        # empty pit on their side. The action consists of the position
        # of the hole and player that is moving.
        actions = []

        b1 = self.board[:self.mancala1]
        b2 = self.board[self.mancala1+1:self.mancala2]

        if self.playerToMove == 1:
            for i in range(len(b1)):
                if b1[i] > 0:
                    actions.append(MancalaAction(self.playerToMove, i))

        else:
            for i in range(len(self.board[self.mancala1+1:self.mancala2])):
                if b2[i] > 0:
                    actions.append(MancalaAction(self.playerToMove, i+self.mancala1+1))
        
        return actions

    def getUtility(self):
        return self.utility

    def getResult(self, action):
        # TODO turn will continue if player lands on their mancala
        state = MancalaState()
        state.board = self.board.copy()
        state.mancala1 = self.mancala1
        state.mancala2 = self.mancala2
        state.player = self.player

        if state.isTerminal():
            s.clearGame()
        
        else: 
            # update board after move
            player = action.getPlayer()
            pit = action.getPit()

            stones = state.board[pit]
            state.board[pit] = 0

            while stones > 0:
                pit += 1
                if pit > state.mancala2:
                    pit = 0
                if player == 1 and pit == state.mancala2:
                    continue
                if player == 2 and pit == state.mancala1:
                    continue
                state.board[pit] += 1
                stones -= 1

            # decide whose move it is
            if player == 1 and pit != state.mancala1:
                state.playerToMove = 2
            elif player == 2 and pit != state.mancala2:
                state.playerToMove = 1
            else:
                state.playerToMove = self.playerToMove

            state.moves = self.moves + 1

        state.updateUtility()

        return state

    def clearGame(self):
        b1 = self.board[:self.mancala1]
        b2 = self.board[self.mancala1+1:self.mancala2]
        comp = []
        for i in range(self.mancala1):
            comp.append(i)
        if b1 == comp:
            for i in b2:
                self.board[self.mancala1] += i
        elif b2 == comp:
            for i in b1:
                self.board[self.mancala2] += i
        
    def isTerminal(self):
        b1 = self.board[:self.mancala1]
        b2 = self.board[self.mancala1+1:self.mancala2]
        comp = []
        for i in range(self.mancala1):
            comp.append(i)
        return b1 == comp or b2 == comp

    def printstate(self):
        b1 = list(map(str, self.board[:self.mancala1]))
        b2 = list(map(str, self.board[self.mancala1+1:self.mancala2]))
        print(' {:^2} {}'.format(self.board[self.mancala2], b2))
        print('    {} {:^2}'.format(b1, self.board[self.mancala1]))
        
