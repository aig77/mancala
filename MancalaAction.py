class MancalaAction:
    def __init__(self, player, pit):
        self.player = player
        self.pit = pit
    
    def getPit(self):
        return self.pit
    
    def getPlayer(self):
        return self.player
    
    def tostring(self):
        return f'Player: {self.player}, Pit: {self.pit}'
