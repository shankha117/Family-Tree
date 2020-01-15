from Member import Member


# this class handles the single instance of the family class
# singleton
class Borg:
    """Borg pattern making the class attributes global"""
    _family_members = {}  # Attribute dictionary
    _message = {}

    def __init__(self):
        self.__dict__ = self._family_members
        self.__dict__ = self._message


"""
The family class handles the 
"""


class Family(Borg):

    def __init__(self):
        Borg.__init__(self)

    """
    this is a composite method which handles the whole process of new member/child addition  to the family 
    """

    def add_child_to_family(self, *args, child: str, sex: str, mother: str):

        # make the mother instance
        mother_instance = self.find_member_by_name(mother)

        if not mother_instance:
            # this is an alpha member
            if args:
                # make the alpha member
                alpha_member = Member(name=child, sex=sex, generation=1)
                # add it to the member dict
                self.add_family_member(alpha_member.name, alpha_member)
        else:
            if mother_instance.sex != "F":
                self._message['message'] = "CHILD_ADDITION_FAILED"
                return self._message

            # if the child has father
            if mother_instance.husband:
                # make the new child instance
                new_child = Member(name=child, sex=sex, mother=mother_instance, father=mother_instance.husband,
                                   generation=mother_instance.generation + 1)

                # add the new child to the family
                self.add_family_member(new_child.name, new_child)

                # add parent for the child
                self.add_parent_for_child(child=new_child, Mother=mother_instance, Father=mother_instance.husband)

                self._message['message'] = "CHILD_ADDITION_SUCCEEDED"

            else:
                # make the new child instance
                new_child = Member(name=child, sex=sex, mother=mother_instance,
                                   generation=mother_instance.generation + 1)

                # add the new child to the family
                self.add_family_member(new_child.name, new_child)

                self._message = "CHILD_ADDITION_SUCCEEDED"

        return self._message

    # child has both mother and father
    def add_parent_for_child(self, child: Member, Mother: Member, Father: Member):

        if child.sex == "M":
            # connect son to mother
            self.add_child_to_mother(mother=Mother, child=child, child_type="sons")

            # connect son to father
            self.add_child_to_father(father=Father, child=child, child_type="sons")
        else:
            # connect daughter to mother
            self.add_child_to_mother(mother=Mother, child=child, child_type="daughters")

            # connect daughter to father
            self.add_child_to_father(father=Father, child=child, child_type="daughters")

    # child has only mother
    def add_only_mother_to_child(self, child: Member, Mother: Member):
        if child.sex == "M":
            # connect son to mother
            self.add_child_to_mother(mother=Mother, child=child, child_type="sons")
        else:
            # connect daughter to mother
            self.add_child_to_mother(mother=Mother, child=child, child_type="daughters")

    # add a child to mother
    def add_child_to_mother(self, mother: Member, child: Member, child_type):

        # append child to list
        getattr(mother, child_type).append(child)
        # update the mother instance in family
        self.update_family_member(mother.name, mother)

    # add a child to father
    def add_child_to_father(self, father: Member, child: Member, child_type):

        # append child to list
        getattr(father, child_type).append(child)

        # update father instance in family
        self.update_family_member(father.name, father)

    def add_marriage_to_family(self, outside_member_name: str, outside_member_sex: str,
                               family_member_instance: Member):

        # make outside member
        outside_member_instance = Member(name=outside_member_name, sex=outside_member_sex,
                                         generation=family_member_instance.generation)

        # add member to instance
        self.add_family_member(outside_member_name, outside_member_instance)

        if outside_member_sex == "M":
            self.add_partner_to_family_member(outside_member_instance, family_member_instance)
        else:
            self.add_partner_to_family_member(family_member_instance, outside_member_instance)

    def add_partner_to_family_member(self, husband: Member, wife: Member):

        # add wife to the husband
        husband.wife = wife

        # update husband
        self.update_family_member(husband.name, husband)

        # add husband to wife
        wife.husband = husband

        # update wife
        self.update_family_member(wife.name, wife)

    def update_family_member(self, name, member):

        self._family_members.update({name: member})

    def add_family_member(self, name, member):

        self._family_members[name] = member

    def find_member_by_name(self, name):

        try:
            member = self._family_members[name]
            return member

        except KeyError as e:
            self._message['message'] = "PERSON_NOT_FOUND"
            return None
