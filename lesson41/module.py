class Stack:

    def __init__(self):
        self.items = []
    
    def show_items(self):
        return self.items

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def push_item(self, item):
        self.items.append(item)
    
    def pop_item(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        else:
            self.items.pop(len(self.items) - 1)
    
    def get_item(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        else:
            res = self.items[len(self.items) - 1]
            self.pop_item()
            return res