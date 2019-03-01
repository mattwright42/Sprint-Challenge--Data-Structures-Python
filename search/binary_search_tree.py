class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        pass

    def breadth_first_for_each(self, cb):
        # initialize queue at self
        bst_queue = [self]

        # loop through queue
        while len(bst_queue):
            # take the first element and put it in a variable
            cur_node = bst_queue.pop(0)
            # check to see if there is a left and add to bst_queue
            if cur_node.left:
                bst_queue.append(cur_node.left)
            # check to see if there is a right and add to bst_queue
            if cur_node.right:
                bst_queue.append(cur_node.right)
            # perform function on the current node
            cb(cur_node.value)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
