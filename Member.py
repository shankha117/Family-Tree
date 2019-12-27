"""
This class holds all the information about a family  member
"""

class Member(object):

    def __init__(self, name, sex, mother=None, father=None, wife=None, husband=None, generation=None):

        self.name = name
        self.sex = sex
        self.father = father
        self.mother = mother
        self.wife = wife
        self.husband = husband
        self.sons = []
        self.daughters = []
        self.generation = generation

    """
    get attribute methods
    """
    def get_father(self):

        return self.father

    def get_mother(self):

        return self.mother

    def get_wife(self):
        return self.wife

    def get_husband(self):
        return self.husband

    def get_sons(self):
        return self.sons

    def get_daughters(self):
        return self.daughters

