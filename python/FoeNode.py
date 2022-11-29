import CharNode

class FoeNode(CharNode):
    def __init(self, priority, maxHP, name, head = None, tail = None):
        super.init(priority, maxHP, name, head, tail)
        self.IS_AI = True
        self.IS_ALLY = False
        self.instructions = "pass"
        self.loadInstructions(name)

    def loadInstructions(self, name):
        #TODO: Check database for name and return instructions as eval string
        pass

    def performTurn(self):
        eval(self.instructions)