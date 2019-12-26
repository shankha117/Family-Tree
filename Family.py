

class Family(object):

    def __init__(self):

        self.members = {}
        # self.relations = []


    def add_new_child_to_family(self,child, mother):

        pass


    def add_marriage(self, husband, wife):

        pass


    def add_family_member(self, name, member):

        self.members[name] = member


    def find_member_by_name(self,name):

        try:
            return self.members[name]

        except KeyError as e:
            return None


