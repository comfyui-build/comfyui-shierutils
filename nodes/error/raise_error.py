# Define the custom error base class
class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

# Define the node class for raising custom errors
class RaiseError:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "BOOL": ("BOOL",),
                "bool": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "error_message": ("STRING", {"default": "CustomError", "multiline": True})
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "execute"
    CATEGORY = "12utils/error"

    def execute(self, trigger, optional_trigger=False, error_name="CustomError"):
        if trigger == optional_trigger:
            # Dynamically create a new exception class with the given name
            error = type(error_name, (CustomError,), {})
            raise error()
        return ()

NODE_CLASS_MAPPINGS = {
    "RaiseError": RaiseError, # 报错
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RaiseErrorNode": "Raise Error",
}

# test
# RaiseErrorNode().execute(True, True, "超出最大边长")