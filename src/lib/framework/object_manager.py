
import importlib


class ObjectManager:
    ALIAS_KEY = 'alias'
    FACTORIES_KEY = 'factories'
    SINGLETON_KEY = 'singleton'

    CONFIGURABLE_FACTORY = 'ConfigurableFactory'
    INVOKABLE_FACTORY = 'InvokableFactory'

    def __init__(self, object_manager_config: dict):
        self._config = dict()
        self._alias = dict()
        self._singleton = dict()
        self._factories = dict()
        self._configurable_params = dict()

        self._object_pool = dict()
        self._build_config(object_manager_config)

    def get(self, name: str):
        name = self._resolve_name(name)

        if name not in self._factories:
            raise Exception('Factory not found for ' + name)

        if self._is_singleton(name) and name in self._object_pool.keys():
            return self._object_pool[name]

        instance = self._create_object(name)

        if self._is_singleton(name):
            self._object_pool[name] = instance

        return instance

    def _create_object(self, name):
        factory = self._factories[name]

        if factory == self.CONFIGURABLE_FACTORY:
            from src.lib.framework import ConfigurableFactory
            factory_instance = ConfigurableFactory()
            arguments = self._configurable_params[name]

            return factory_instance(self, name, arguments)

        elif factory == self.INVOKABLE_FACTORY:
            from src.lib.framework import InvokableFactory
            factory_instance = InvokableFactory()

        else:
            module_name, factory_name = factory.rsplit(".", 1)
            module = importlib.import_module(module_name)
            factory_class = getattr(module, factory_name)
            factory_instance = factory_class()

        return factory_instance(self, name)

    def _build_config(self, object_manager_config):
        self._config = object_manager_config

        if self.ALIAS_KEY in object_manager_config.keys():
            self._alias = object_manager_config[self.ALIAS_KEY]

        if self.FACTORIES_KEY in object_manager_config.keys():
            self._factories = object_manager_config[self.FACTORIES_KEY]

        if self.SINGLETON_KEY in object_manager_config.keys():
            self._singleton = object_manager_config[self.SINGLETON_KEY]

        if self.CONFIGURABLE_FACTORY in object_manager_config.keys():
            self._configurable_params = object_manager_config[self.CONFIGURABLE_FACTORY]
            # add configurable factory
            for class_name in self._configurable_params.keys():
                self._factories[class_name] = self.CONFIGURABLE_FACTORY

    def _resolve_name(self, name):
        if name in self._alias.keys():
            return self._alias[name]
        return name

    def _is_singleton(self, name):
        if name in self._singleton.keys():
            return bool(self._singleton[name])
        return True
