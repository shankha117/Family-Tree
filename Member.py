class Member(object):

    def __init__(self, name, sex, mother=None, wife=None, husband=None):

        self.name = name
        self.sex = sex
        # self.father = father
        self.mother = mother
        self.wife = wife
        self.husband = husband
        self.sons = []
        self.daughters = []
        self.generation = None


    def add_child(self, child_name, mother_name, sex:str):
        pass

    def add_father(self, father):
        self.father = father

    def add_mother(self, mother):
         pass

    def add_wife(self, husband):
         pass

    def add_husband(self, wife):
        pass

    def add_generation(self, gen:int):
        pass

    def add_relations(self, relation):
        pass

