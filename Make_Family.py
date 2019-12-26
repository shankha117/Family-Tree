from Family import Family
from Member import Member
from resources.seed_data import family,alpha

class MakeFamily(object):

    def __init__(self):

        self.make_family()

    def make_family(self):


        for i in alpha:

            if not i['partner']:
                self.new_child(i['name'], i['sex'], i['mother'],"alpha")

        for i in family:

            if i['mother']:

                self.new_child(i["name"], i["mother"], i["sex"])

            else:
                pass


    def new_alpha(self, child_name: str, sex: str,mother_name: str):

        Family().add_new_child_to_family(child=child_name,sex= sex, mother=mother_name,)





    def new_child(self, child_name: str, sex: str,mother_name: str):


        Family().add_new_child_to_family(child=child_name,sex= sex, mother=mother_name,)

    def new_marriage(self, husband, wife):
        pass


if __name__== "__main__": MakeFamily()