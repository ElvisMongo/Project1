from abc import ABCMeta, abstractmethod
import os
import pickle
import json


class ParamHandlerException(BaseException):
    pass


class ParamHandler(metaclass=ABCMeta):  # создаем абстрактный класс
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod  # помечаем метод как абстрактный
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass))

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))

        return klass(source, *args, **kwargs)


class JsonParamHandler(ParamHandler):
    def read(self):
        """
        Чтение в формате JSON и присвоение значений в self.params
        """
        with open(self.source) as f:
            a = json.load(f)
            for i in a:
                self.params[i] = a[i]

    def write(self):
        """
        Запись в формате JSON параметров self.params
        """
        with open(self.source, "w") as f:
            json.dump(self.params, f)


class PickleParamHandler(ParamHandler):
    def read(self):
        """
        Чтение в формате pickle и присвоение значений в self.params
        """
        with open(self.source, "rb") as f:
            a = pickle.load(f)
            for i in a:
                self.params[i] = a[i]

    def write(self):
        """
        Запись в формате pickle параметров self.params
        """
        with open(self.source, "wb") as f:
            pickle.dump(self.params, f)


    def read(self, source):
        with open('my_file.json', 'r') as f:
            self.source = json.load(f)


config = ParamHandler.get_instance('./params.json')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()
config.read()

config = ParamHandler.get_instance('./params.pickle')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()
config.read()