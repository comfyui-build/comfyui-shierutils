from importlib import import_module
from collections import defaultdict
import os

nodes_dict = defaultdict(list)
nodes_path = os.path.join(os.path.dirname(__file__), 'nodes')

for root, dirs, files in os.walk(nodes_path):
    for file in files:
        if file.endswith('.py'):
            try:
                nodes_dict[root.split(os.sep)[-1]].append(file[:-3])
            except KeyError:
                nodes_dict[root.split(os.sep)[-1]] = []
                nodes_dict[root.split(os.sep)[-1]].append(file[:-3])

# print(nodes_dict)

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for key,value in nodes_dict.items():
    for module_name in value:
        imported_module = import_module(".nodes.{}.{}".format(key,module_name), __name__)

        NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
        NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
