

class Relation_edges(object):

    marriage = 1
    child = 2


    def __init__(self, relation=None, from_Node=None, to_Node=None, generation=None):

        self.value = relation
        self.from_node = from_Node
        self.to_node = to_Node
        self.generation = generation


    """
    marriage relations are always -
        
        hunsband ---> wife
        
    """
    def get_husband(self, relation):

        if relation.value == 1:

            return relation.from_node


    def get_wife(self, relation):

        if relation.value == 1:

            return relation.to_node

    """
    child relations are always-
        
        mother --> child    
    """
    def get_son(self, relation):

        if relation.value == 2:

            return relation.to_node

    def get_mother(self, relation):

        if relation.value == 2:

            return relation.from_node