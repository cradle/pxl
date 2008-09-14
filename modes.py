import campaign

class MainGameState(campaign.GameState):
    def __init__(self,driver,screen,level=0):
    	campaign.GameState.__init__(self,driver,screen,level)
