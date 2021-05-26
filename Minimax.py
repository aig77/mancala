import random
import sys
from MancalaAction import MancalaAction

class Minimax:

    def __init__(self, depth):
        self.numberOfStates = 0
        self.depth = depth

    def minimaxDecision(self, state):
        # player 1 is maximizing agent
        # player 2 is minimizing agent

        # computer minimizes
        min_v = float('inf')
        best_action = None
        for a in state.getActions():
            v = self.minimax(state.getResult(a), self.depth, float('-inf'), float('inf'))
            if v < min_v:
                best_action = a
                min_v = v

        return best_action
                

    def minimax(self, state, depth, alpha, beta):
        if depth == 0 or state.isTerminal():
            return state.getUtility()
        
        if state.playerToMove == 1:
            max_v = float('-inf')
            for a in state.getActions():
                v = self.minimax(state.getResult(a), depth-1, alpha, beta)
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return max_v

        else:
            min_v = float('inf')
            for a in state.getActions():
                v = self.minimax(state.getResult(a), depth-1, alpha, beta)
                min_v = min(min_v, v)
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return min_v
            
