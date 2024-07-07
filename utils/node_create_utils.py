#from folder_paths import base_path as comfyui_path
import os
comfyui_path = r"E:\code\comfyui_nodes\ComfyUI"
custom_nodes_path = os.path.join(comfyui_path, 'custom_nodes')
sherpath = os.path.join(custom_nodes_path, 'comfyui-shierutils')
print(sherpath)

def category():
    current_path = os.path.abspath(__file__)
    parent_folder_name = os.path.basename(os.path.dirname(current_path))
    CATEGORY = parent_folder_name
    return CATEGORY

def nodename():
    current_path = os.path.abspath(__file__)
    node_name = os.path.basename(current_path).replace('.py', '')
    node_name = node_name.replace('_', ' ')
    return node_name