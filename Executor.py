from abc import ABC, abstractmethod
from helper import get_command_and_entity, get_class_object
from constants import Operations, Relations, Module, Class


class Execute(object):

    def __init__(self, operation):
        self.op = operation

        # mapping for the Executors
        self._mappings = {
            Operations.ADD.value: {"module": Module.executor.value,
                                   "class": Class.add.value},

            Operations.GET.value: {"module": Module.executor.value, "class": Class.get.value},
        }

    def start(self):
        command, entity = get_command_and_entity(self.op)

        class_object = get_class_object(self._mappings[command]['module'], self._mappings[command]['class'])

        class_object.start(entity)


class AbstractExecutor(ABC):

    @abstractmethod
    def start(self, entity_list):
        pass

    @abstractmethod
    def perform_task(self, main_entity, *args):
        pass

    def get_main_entity(self, entity):
        print("Thsi si new")


class AddChild(AbstractExecutor, ABC):

    def start(self, entity_list):
        mother = entity_list[0]

        super(self.__class__, self).get_main_entity(mother)

        child = entity_list[1]

        gender = entity_list[2]

    def perform_task(self, main_entity, *args):
        print("--hii")


class GetRelation(AbstractExecutor, ABC):

    def start(self, entity_list):
        mother = entity_list[0]

        super(self.__class__, self).get_main_entity(mother)

        # child = entity_list[1]
        #
        # gender = entity_list[2]

    def perform_task(self, main_entity, *args):
        print("--hii")