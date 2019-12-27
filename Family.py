from Member import Member

class Borg:
    """Borg pattern making the class attributes global"""
    _family_members = {} # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._family_members


class Family(Borg):

    def __init__(self):
        Borg.__init__(self)

    def add_child_to_family(self, *args, child: str, sex: str, mother: str):

        # if alpha member
        mother_instance = self.find_member_by_name(mother)

        if not mother_instance:
            # this is an alpha member
            if args:
                # make the alpha member
                alpha_member = Member(name=child, sex=sex,generation=1)
                # add it to the member dict
                self.add_family_member(alpha_member.name,alpha_member)
        else:
            print(child,mother)
            print(vars(mother_instance))

        # if no mother found --> return false
        # "no female member found of this name"


    def add_marriage_to_family(self, outside_member_name: str, outside_member_sex:str, family_member_instance:Member):

        # make outside member
        outside_member_instance = Member(name=outside_member_name, sex=outside_member_sex, generation=family_member_instance.generation)

        # add member to instance
        self.add_family_member(outside_member_name,outside_member_instance)

        if outside_member_sex == "M":
            self.add_partner_to_family_member(outside_member_instance,family_member_instance)
        else:
            self.add_partner_to_family_member(family_member_instance,outside_member_instance)

    def add_partner_to_family_member(self, husband:Member, wife:Member):

        # add wife to the husband
        husband.wife = wife

        # update husband
        self.update_family_member(husband.name, husband)

        # add husband to wife
        wife.husband = husband

        # update wife
        self.update_family_member(wife.name, wife)

    def update_family_member(self, name, member):

        self._family_members.update({name:member})

    def add_family_member(self, name, member):
        self._family_members[name] = member

    def find_member_by_name(self,name):

        try:
            return self._family_members[name]

        except KeyError as e:
            return None


