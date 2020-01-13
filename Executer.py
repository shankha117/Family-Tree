from abc import ABC, abstractmethod
from helper import get_command_and_entity
from constants import Operations, Relations, Module, Class
import importlib

class AbstractExecutor(ABC):

    @abstractmethod
    def start(self,entity_list):
        pass

    @abstractmethod
    def get_main_entity(self, entity):
        pass

    @abstractmethod
    def perform_task(self, main_entity, *args):
        pass


class Execute(object):

    def __init__(self, operation):

        self.op = operation

        # mapping for the Executors

        _mappings = {
            Operations.ADD: {"module": MODULE_ICE_QNA_EXCEL_EXTRACTOR,
                                        "class": AddChild},
            Operations.GET: {"module": MODULE_ICE_QNA_CSV_EXTRACTOR, "class": CLASS_ICE_QNA_CSV_EXTRACTOR},
        }

    def start(self):
        command, entity = get_command_and_entity(self.op)



class AddChild(AbstractExecutor, ABC):

    def start(self,entity_list):
        mother = entity_list[0]

        self.get_main_entity(mother)
        self.blass()
        child = entity_list[1]

        gender = entity_list[2]

    def get_main_entity(self, main_entity: str):
        print("hii")


    def blass(self):
        print("hii")