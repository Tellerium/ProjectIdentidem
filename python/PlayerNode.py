import CharNode

class PlayerNode(CharNode):
    def __init(self, priority, maxHP, name, head = None, tail = None):
        super.init(priority, maxHP, name, head, tail)
        self.IS_AI = False
        self.IS_ALLY = True
