'''
author:
    shiertier

overview:
    This node defines a mechanism for raising custom errors in ComfyUI nodes. It includes a custom error base class and a node class that can be used to trigger custom errors based on input conditions.

input:
    BOOL(bool): A boolean input that determines whether to raise an error.
    matching(bool, optional): A boolean input that determines the matching condition for raising the error. Default is False.
    error_message(str, optional): A string input that specifies the error message to be raised. Default is "CustomError".

output:
    None

# zh
功能:
    此节点定义了在ComfyUI节点中引发自定义错误的机制。它包括一个自定义错误基类和一个节点类，可以根据输入条件触发自定义错误。

输入:
    BOOL(bool): 一个布尔输入，用于确定是否引发错误。
    matching(bool, 可选): 一个布尔输入，用于确定引发错误的匹配条件。默认为False。
    error_message(str, 可选): 一个字符串输入，用于指定要引发的错误信息。默认为"CustomError"。

输出:
    无
'''

# Define the custom error base class
class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

# Define the node class for raising custom errors
class RaiseErrorBase:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "BOOL": ("BOOL",),
                "matching": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "error_message": ("STRING", {"default": "CustomError", "multiline": True})
            }
        }
    OUTPUT_NODE = True
    FUNCTION = "execute"
    CATEGORY = "error"

    def execute(self, BOOL, matching=True, error_message="CustomError"):
        if BOOL == matching:
            raise CustomError(error_message)

NODE_CLASS_MAPPINGS = {
    "RaiseError": RaiseErrorBase, # 报错
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RaiseErrorNode": "Raise Error",
}