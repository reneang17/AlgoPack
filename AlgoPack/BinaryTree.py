
class BNode:
    def __init__(self, value= None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_right_child(self, right_node):
        self.right = right_node

    def set_left_child(self, left_node):
        self.left = left_node

    def set_right_child(self, right_node):
        self.right = right_node

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None
