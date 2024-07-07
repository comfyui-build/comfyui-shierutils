from importlib import import_module

node_list = {
    'image': ['verify_img_side','get_img_size'],
    'tutorial': ['example'],
    'error': ['raise_error']
}

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for key,value in node_list.items():
    for module_name in value:
        imported_module = import_module(".nodes.{}.{}".format(key,module_name), __name__)

        NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
        NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']