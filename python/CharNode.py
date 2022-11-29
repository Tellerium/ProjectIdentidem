import TwoWayNode

class CharNode(TwoWayNode):
    def __init__(self, priority, maxHP, name, head = None, tail = None):
        super.init(self, head, tail)
        self.IS_AI = False
        self.IS_ALLY = False
        self.name = name
        self.priority = priority
        self.maxHP = maxHP
        self.battleHP = maxHP
        self.abilityList = []
        
    def getAI(self):
        return self.IS_AI
    
    def getAlly(self):
        return self.IS_ALLU

    def setMaxHP(self, newMax):
        self.maxHP = newMax
        
    def getMaxHP(self):
        return self.maxHP
    
    def setBattleHP(self, newHP):
        return self.newHP

    def getBattleHP(self):
        return self.battleHP
    
    def damage(self, damInt):
        self.battleHP -= damInt
    
    def setAbilityList(self, newList):
        self.abilityList = newList
    
    def getAbilityList(self):
        return self.abilityList()

    def addAbility(self, newAbility):
        self.abilityList.append(newAbility)
    
    def removeAbility(self, targetAbility):
        self.abilityList.remove(targetAbility)
    
    def performTurn(self):
        pass