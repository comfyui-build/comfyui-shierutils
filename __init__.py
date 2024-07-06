from .nodes.compare.verify_img_side import VerifyImageSide
from .nodes.tutorial.example import a1, a2, a3, a4
from .nodes.error.raise_error import RaiseErrorNode

NODE_CLASS_MAPPINGS = {
    "RaiseErrorNode": RaiseErrorNode,
    "a1": a1,"a2": a2,"a3": a3,"a4":a4,
    "VerifyImageSide": VerifyImageSide,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RaiseErrorNode": "Raise Custom Error", # 报错
    "a1": "a1基础格式","a2": "a2基础数据类型","a3": "a3基础调用流程","a4":"a4一个可以运行的节点", # 教程示例
    "VerifyImageSide": "Verify Image Side", # 验证图片边长
}