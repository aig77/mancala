from MancalaAction import MancalaAction

class MancalaState:

    def __init__(self, pits=3, stones=3):
        # boards portray the current position of the game
        # the numbers represent the number of stones in each players' pits
        self.board = self.initBoard(pits, stones)
        # positon of the mancalas in the board array
        self.mancala1 = pits
        self.mancala2 = pits*2 + 1
        self.player = 1 # human player = 1, cpu = 2
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
        self.utility = self.board[self.mancala1] - self.board[self.mancala2]

    def getUtility(self):
        return self.utility

    def getActions(self):
        # For Mancala, each player has one valid action for every non
        # empty pit on their side. The action consists of the position
        # of the hole and player that is moving.
        actions = []

        b1 = self.board[:self.mancala1]
        b2 = self.board[self.mancala1+1:self.mancala2]

        if self.playerToMove == self.player:
            for i in range(len(b1)):
                if b1[i] > 0:
                    actions.append(MancalaAction(self.playerToMove, i))

        else:
            for i in range(len(b2)):
                if b2[i] > 0:
                    actions.append(MancalaAction(self.playerToMove, i+self.mancala1+1))
        
        return actions


    def getResult(self, action):
        # TODO turn will continue if player lands on their mancala
        state = MancalaState()
        state.board = self.board.copy()
        state.mancala1 = self.mancala1
        state.mancala2 = self.mancala2
        state.player = self.player
         
        # update board after move
        player = action.getPlayer()
        pit = action.getPit()

        stones = state.board[pit]
        state.board[pit] = 0

        # going around and adding stones
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


        # stealing
        comp = []
        j = state.mancala2-1
        for i in range(state.mancala1):
            comp.append(j)
            j-=1
        
        if player == 1 and pit < state.mancala1 and state.board[pit]-1 == 0:
            state.board[pit] = 0
            stolen = state.board[comp[pit]]
            state.board[comp[pit]] = 0
            state.board[state.mancala1] += stolen + 1
        elif player == 2 and pit > state.mancala1 and pit < state.mancala2 and state.board[pit]-1 == 0:
            state.board[pit] = 0
            stolen = state.board[comp.index(pit)]
            state.board[comp.index(pit)] = 0
            state.board[state.mancala2] = stolen + 1

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
         for i in range(len(self.board)):
            if i < self.mancala1:
                self.board[self.mancala1] += self.board[i]
                self.board[i] = 0
            elif i > self.mancala1 and i < self.mancala2:
                self.board[self.mancala2] += self.board[i]
                self.board[i] = 0
        
    def isTerminal(self):
        b1 = self.board[:self.mancala1]
        b2 = self.board[self.mancala1+1:self.mancala2]
        comp = []
        for i in range(self.mancala1):
            comp.append(0)
        return b1 == comp or b2 == comp

    def printstate(self):
        b1 = list(map(str, self.board[:self.mancala1]))
        b2 = list(map(str, self.board[self.mancala1+1:self.mancala2]))[::-1]
        print(' {:^2} {}'.format(self.board[self.mancala2], b2))
        print('    {} {:^2}'.format(b1, self.board[self.mancala1]))
        
