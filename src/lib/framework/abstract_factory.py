
import importlib


class ConfigurableFactory:

    def __call__(self, object_manager, name, arguments):
        module_name, class_name = name.rsplit(".", 1)

        module = importlib.import_module(module_name)
        object_class = getattr(module, class_name)

        args = list()
        for arg in arguments:
            args.append(object_manager.get(arg))

        return object_class(*args)


class InvokableFactory:

    def __call__(self, object_manager, name):
        module_name, class_name = name.rsplit(".", 1)

        module = importlib.import_module(module_name)
        object_class = getattr(module, class_name)

        return object_class()
