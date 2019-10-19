import sys
import importlib

name = sys.argv[1]
module = importlib.import_module(name)
class_ = getattr(module, name)
class_.create_table()
