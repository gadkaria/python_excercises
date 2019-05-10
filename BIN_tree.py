class Tree:
    # Tree Constructor
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

def rotate_right(node):
    # Create temp Node which is a copy of the left
    temp = node.left

    # Break connection and set old right to be the left of temp
    node.left = temp.right

    #set right of temp to the beginning node
    temp.right = node

    # Would also need to fix the height of each node, especially temp and temp.left

    #return temp and fix tree on the outside
    return temp 

def rotate_left(node):
    #create a temporary Node to be the same as the right node
    temp = node.right

    # break the connection to the old right node. 
    # Set it to the left of the temp if the left exists else it will be None
    node.right = temp.left

    # set the left of the temp node to be the highest node
    temp.left = node

    # Would also need to fix the height of each node, especially temp and temp.left

    #return the temp node and set it as the node that was passed in
    return temp


    