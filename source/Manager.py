# AbstractManager (Main package)

# This class provides base
# for managers which should
# be singleton classees

# Date: 24/11/2018
# Author: Mikołaj Bednarek

class AbstractManager:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(AbstractManager, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
