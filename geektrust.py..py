# This is the EntryPoint

from Make_Family import MakeFamily

class EntryPoint(object):


    def __init__(self):

        # initialize the Family Tree
        MakeFamily()

        ## TODO need to add a chain of responsibility here


    def make_family_tree(self):
        pass

    def read_operations(self,file_path):

        file = open(file_path,'r')
        file_strings = file.read()
        file.close()
        operation_list = file_strings.split("\n")[:-1]

        pass

    def perform_operations(self):
        pass




if __name__== "__main__":
  EntryPoint()