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
        if self.father:
            print(self.father.name)
        else:
            print(None)

    def get_mother(self):
        if self.mother:
            return self.mother.name
        else:
            return None

    def get_wife(self):
        if self.wife:
            return self.wife.name
        else:
            return None

    def get_husband(self):
        if self.husband:
            return self.husband
        else:
            print(None)

    def get_sons(self):
        if self.sons:
            # print the output in required fashion
            for i in self.sons:
                print(i.name, end=" ")
            print("")
        else:
            print(None)

    def get_daughters(self):
        if self.daughters:
            # print the output in required fashion
            for i in self.daughters:
                print(i.name, end=" ")
            print("")
        else:
            print(None)

    def get_paternal_uncle(self):

        # if self.father:
        #     if self.father.
        pass

    def get_maternal_uncle(self):
        pass


    def get_siblings(self):

        if self.mother:
            siblings = []



    def get_brothers(self):
        if self.mother.sons:
            return self.mother.sons


    def get_sisters(self):
        if self.mother.daughters:
            return self.mother.daughters
