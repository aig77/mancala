import random
import sys
from MancalaAction import MancalaAction

class Minimax:

    def __init__(self, depth):
        self.numberOfStates = 0
        self.depth = depth

    def MinimaxDecision(self, state):
        self.numberOfStates = 0

        max_v = float('-inf')
        best_action = None
        for a in state.getActions():
            v = self.MinValue(state.getResult(a), float('-inf'), float('inf'), self.depth)
            if v > max_v:
                best_action = a
                max_v = v
        return best_action

    def MinValue(self, state, alpha, beta, depth):
        self.numberOfStates += 1

        if depth == 0 or state.isTerminal():
            return state.getUtility()
        v = float('inf')
        for a in state.getActions():
            v = min(v, self.MaxValue(state.getResult(a), alpha, beta, depth - 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def MaxValue(self, state, alpha, beta, depth):
        self.numberOfStates += 1
        if depth == 0 or state.isTerminal():
            return state.getUtility()
        v = float('-inf')
        for a in state.getActions():
            v = max(v, self.MinValue(state.getResult(a), alpha, beta, depth - 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v