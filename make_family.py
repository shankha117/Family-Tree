from family import Family
from resources.seed_data import family_data, alpha_data


class MakeFamily(object):

    def __init__(self):

        self.make_family()

    def make_family(self):

        # add alpha king to family

        Family().add_child_to_family("alpha", child=alpha_data[0]['name'], sex=alpha_data[0]['sex'],
                                     mother=alpha_data[0]['mother'])

        # # add alpha queen to the family
        self.add_marriage_with_family_member(outsider_name=alpha_data[1]['name'],
                                             outsider_sex=alpha_data[1]['sex'],
                                             family_member=alpha_data[1]['partner'])

        for i in family_data:

            if i['mother']:

                self.add_child(child_name=i["name"], sex=i["sex"], mother_name=i["mother"])

            else:

                self.add_marriage_with_family_member(outsider_name=i['name'],
                                                     outsider_sex=i['sex'],
                                                     family_member=i['partner'])

    @staticmethod
    def add_child(child_name: str, sex: str, mother_name: str, ):

        Family().add_child_to_family(child=child_name, sex=sex, mother=mother_name)

    @staticmethod
    def add_marriage_with_family_member(outsider_name: str, outsider_sex: str, family_member: str):

        family_member_instancec = Family().find_member_by_name(family_member)

        if family_member_instancec:
            Family().add_marriage_to_family(outside_member_name=outsider_name, outside_member_sex=outsider_sex,
                                            family_member_instance=family_member_instancec)

# if __name__== "__main__": MakeFamily()
