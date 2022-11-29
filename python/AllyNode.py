import CharNode
import Globals

class AllyNode(CharNode):
    def __init(self, priority, maxHP, name, head = None, tail = None):
        super.init(priority, maxHP, name, head, tail)
        self.IS_AI = True
        self.IS_ALLY = True
        self.instructions = "pass"
        self.loadInstructions(name)

    def loadInstructions(self, name):
        for item in Globals.charRoot.findall('./friends'):
            for child in item:
                if child.tag == name:
                    self.instructions = child.text

    def performTurn(self):
        eval(self.instructions)
