import importlib


def get_command_and_entity(operation):
    split = operation.split()

    return split[0], split[1:]


def get_class_object(module_name, class_name):

    # import the module
    module = importlib.import_module(module_name)

    # load the class
    class_object = getattr(module, class_name)()

    return class_object
