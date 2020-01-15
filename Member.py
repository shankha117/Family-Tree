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
            return self.father.name
        else:
            return None

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

    def get_siblings(self):
        if self.get_mother():
            # make the siblings list with all brothers and sisters from the same mother
            # as all mother-child connection is guaranteed
            siblings = self.get_brothers() + self.get_sisters()

            # remove itself from the list
            siblings.remove(self)
            if siblings:
                for i in siblings:
                    print(i.name, end=" ")
                print("")
                return
        print(None)

    def get_brothers(self):
        if self.mother:
            return self.mother.sons

    def get_sisters(self):
        if self.mother:
            return self.mother.daughters

    def get_paternal_uncle(self):

        if self.get_father():
            # we need to make sure father is a actual member of the family
            if self.father.get_mother():
                # get fathers brothers
                paternal_uncles = self.father.get_brothers()

                # exclude father from paternal uncles
                paternal_uncles.remove(self.father)

                if paternal_uncles:
                    for i in paternal_uncles:
                        print(i.name, end=" ")
                    print("")
                    return
        print(None)

    def get_paternal_aunt(self):

        if self.get_father():
            # we need to make sure father is a actual member of the family
            if self.father.get_mother():
                # get fathers sisters
                paternal_aunt = self.father.get_sisters()

                if paternal_aunt:
                    for i in paternal_aunt:
                        print(i.name, end=" ")
                    print("")
                    return
        print(None)

    def get_maternal_uncle(self):

        if self.get_mother():
            # we need to make sure father is a actual member of the family
            if self.mother.get_mother():
                # get mothers brothers
                maternal_uncle = self.mother.get_brothers()
                if maternal_uncle:
                    for i in maternal_uncle:
                        print(i.name, end=" ")
                    print("")
                    return
        print(None)

    def get_maternal_aunt(self):

        if self.get_mother():
            # we need to make sure father is a actual member of the family
            if self.mother.get_mother():
                # get mothers sisters
                maternal_aunt = self.mother.get_sisters()

                # exclude mother from maternal aunts
                maternal_aunt.remove(self.mother)

                if maternal_aunt:
                    for i in maternal_aunt:
                        print(i.name, end=" ")
                    print("")
                    return
        print(None)

    def get_sister_in_law(self):

        pass

    def get_brother_in_law(self):
        pass