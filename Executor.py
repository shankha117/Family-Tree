from abc import ABC, abstractmethod

from Family import Family
from helper import get_command_and_entity, get_class_object
from constants import Operations, Relations, Module, Class, Methods


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

        # super(self.__class__, self).get_main_entity(mother)

        child = entity_list[1]

        gender = entity_list[2]

        self.perform_task(mother, child, gender)

    def perform_task(self, main_entity, *args):
        res = Family().add_child_to_family(child=args[0], sex=args[1], mother=main_entity)

        print(res['message'])


class GetRelation(AbstractExecutor, ABC):

    def __init__(self):

        self._mappings = {
            Relations.son.value: {"method": Methods.son.value},

            Relations.pu.value: {"class": Class.get.value},
            Relations.mu.value: {},
            Relations.pa.value: {},
            Relations.ma.value: {},
            Relations.sil.value: {},
            Relations.bil.value: {},
            Relations.s.value: {},
            Relations.d.value: {}
        }

    def start(self, entity_list):
        member = entity_list[0]
        # super(self.__class__, self).get_main_entity(member)
        if not Family().find_member_by_name(member):
            print("PERSON_NOT_FOUND")
        else:
            relation = entity_list[1]

            self.perform_task(member, relation)

    def perform_task(self, main_entity, *args):

        member_object = Family().find_member_by_name(main_entity)

        member_object.__getattribute__(self._mappings[args[0]]['method'])()


