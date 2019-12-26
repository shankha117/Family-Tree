from Family import Family
from Member import Member
from resources.seed_data import family

class MakeFamily(Family, Member):


    def make_family(self):

        for i in family:
            print(i)
