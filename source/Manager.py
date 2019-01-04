# AbstractManager (Main package)

# This class provides base
# for managers which should
# be singleton classees

# Date: 24/11/2018
# Author: Mikołaj Bednarek

class AbstractManager:
    _instance = None
    def __new__(cls, *args, **kw):
        print("New instance")
        if not isinstance(cls._instance, cls):
            print("New object")
            cls._instance = object.__new__(cls, *args, **kw)
        else:
            print("Old object")
        return cls._instance
