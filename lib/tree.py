class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if self.root is None:
            return None

        result = [self.root]

        while result:
            node = result.pop(0)
            if node.get('id') == id:
                return node
            children = node.get('children', [])
            for child in children:
                result.append(child)

        return None
