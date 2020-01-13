# This is the EntryPoint
import sys
from Make_Family import MakeFamily
from Executor import Execute
from Family import Family
import traceback

class EntryPoint(object):

    def __init__(self, file_path: str):

        self.path = file_path
        self.operations = []

        # initialize the Family Tree
        self.make_family_tree()

        # read the operations
        self.read_operations()

        # perform the operations
        self.perform_operations()

        ## TODO need to add a chain of responsibility here

    def make_family_tree(self):

        try:
            MakeFamily()
        except Exception as e:
            print(traceback.format_exc(str(e)))

    def read_operations(self):
        try:
            # read the file
            file = open(self.path, 'r')
            file_strings = file.read()
            file.close()

            # split the file
            self.operations = file_strings.split("\n")[:]

        except Exception as e:
            print(traceback.format_exc(str(e)))

    def perform_operations(self):

        try:
            for i in self.operations:

                Execute(i).start()

        except Exception as e:
            print(traceback.format_exc(str(e)))

if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise Exception(
            """the input format is ----
        python -m geektrust <absolute path to the input file>""")

    EntryPoint(sys.argv[1])
