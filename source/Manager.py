# AbstractManager (Main package)

# This class provides base
# for managers which should
# be singleton classees

# Date: 24/11/2018
# Author: Mikołaj Bednarek

class AbstractManager:
    _instance = None
    def __new__(cls, *args, **kw):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
