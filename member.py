"""
This class holds all the information about a family  member
"""
from constants import Gender


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

    @staticmethod
    def print_list(data):
        for i in data:
            print(i.name, end=" ")
        print("")

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
            self.print_list(self.sons)
            # for i in self.sons:
            #     print(i.name, end=" ")
            # print("")
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

    def find_siblings(self):
        if self.get_mother():
            # make the siblings list with all brothers and sisters from the same mother
            # as all mother-child connection is guaranteed
            siblings = self.get_brothers() + self.get_sisters()

            # remove itself from the list
            siblings.remove(self)
            if siblings:
                return siblings
        return None

    def get_siblings(self):
        siblings = self.find_siblings()
        if siblings:
            self.print_list(siblings)
        else:
            print(siblings)

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
                paternal_uncles = self.father.get_brothers()[:]

                # exclude father from paternal uncles
                paternal_uncles.remove(self.father)

                if paternal_uncles:
                    self.print_list(paternal_uncles)
                    return
        print(None)

    def get_paternal_aunt(self):

        if self.get_father():
            # we need to make sure father is a actual member of the family
            if self.father.get_mother():
                # get fathers sisters
                paternal_aunt = self.father.get_sisters()[:]

                if paternal_aunt:
                    self.print_list(paternal_aunt)
                    return
        print(None)

    def get_maternal_uncle(self):

        if self.get_mother():
            # we need to make sure father is a actual member of the family
            if self.mother.get_mother():
                # get mothers brothers
                maternal_uncle = self.mother.get_brothers()[:]
                if maternal_uncle:
                    self.print_list(maternal_uncle)
                    return
        print(None)

    def get_maternal_aunt(self):

        if self.get_mother():
            # we need to make sure father is a actual member of the family
            if self.mother.get_mother():
                # get mothers sisters
                maternal_aunt = self.mother.get_sisters()[:]

                # exclude mother from maternal aunts
                maternal_aunt.remove(self.mother)

                if maternal_aunt:
                    self.print_list(maternal_aunt)
                    return
        print(None)

    def get_sister_in_law(self):
        res = self.get_spouse_sisters() + list(i for i in self.get_wives_of_siblings() if i)
        self.print_list(res)

    def get_brother_in_law(self):
        res = self.get_spouse_brothers() + list(i for i in self.get_husband_of_siblings() if i)
        self.print_list(res)

    def get_spouse_sisters(self):

        # if member is male
        if self.sex == Gender.Male.value:
            if self.wife:
                return self.wife.get_sisters()
                # return list(i.name for i in self.wife.get_sisters())

            return []

        # is member is female
        else:
            if self.husband:
                return self.husband.get_sisters()
                # return list(i.name for i in self.husband.get_sisters())

            return []

    def get_spouse_brothers(self):

        # if member is male
        if self.sex == Gender.Male.value:
            if self.wife:
                return self.wife.get_brothers()
                # return list(i.name for i in self.wife.get_brothers())

            return []

        # is member is female
        else:
            if self.husband:
                return self.husband.get_brothers()
                # return list(i.name for i in self.husband.get_brothers())

            return []

    def get_wives_of_siblings(self):

        try:
            for i in self.find_siblings():
                if i.wife:
                    yield i.wife

        except Exception as e:
            yield

    def get_husband_of_siblings(self):

        try:
            for i in self.find_siblings():
                if i.husband:
                    yield i.husband

        except Exception as e:
            yield
