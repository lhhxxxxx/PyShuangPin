from enum import Enum
import os
import importlib


class Register(dict):
    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        self._dict = {}

    def register(self, target):
        def add_register_item(key, value):
            if not callable(value):
                raise Exception(f"register object must be callable! But receive:{value} is not callable!")
            if key in self._dict:
                print(f"warning: \033[33m{value.__name__} has been registered before, so we will override it\033[0m")
            self[key] = value
            return value

        if callable(target):
            return add_register_item(target.__name__, target)
        else:
            return lambda x: add_register_item(target, x)

    def __call__(self, target):
        return self.register(target)

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __getitem__(self, key):
        return self._dict[key]

    def __contains__(self, key):
        return key in self._dict

    def __str__(self):
        return str(self._dict)

    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()


class Style(Enum):
    NORMAL = 0
    TONE = 8
    INITIALS = 3
    FINALS = 5
    FINALS_TONE = 9


finals_register = Register()
initials_register = Register()
zero_initial_finals_register = Register()

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and not file.startswith("__"):
        importlib.import_module(f"pyshuangpin.modules.{file[:-3]}")
