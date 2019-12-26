from Member import Member

class Family(object):

    def __init__(self):

        self.members = {}
        # self.relations = []


    def add_new_child_to_family(self, child: str, sex: str, mother: str,*args):

        # if alpha member
        print(self)
        print(self.members)
        print(child, sex, mother, args)

        mother = self.find_member_by_name(mother)

        if not mother:
            # this is an alpha member

            if args:
                alpha_member = Member(child, sex)
                print("NEW MEMBER ADDED",alpha_member)




        # if no mother found --> return false
        # "no female member found of this name"





    def add_marriage(self, husband, wife):

        pass



    def add_family_member(self, name, member):

        self.members[name] = member


    def find_member_by_name(self,name):

        try:
            return self.members[name]

        except KeyError as e:
            return None


