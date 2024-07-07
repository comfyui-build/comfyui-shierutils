'''
VerifyImage插件。
输入
    # 名称 | 类型 | 默认值
    image | image
    对象 | 下拉菜单选择 （短边最小值，长边最长值， 像素总值） | 短边最小值
    方式 | 下拉菜单选择 （>,>=,=,<,<=）| >
    数值 | int | 256
输出
    bool | booler
功能
    按方式比较对象和数值，返回真或假
'''

class VerifyImageSide:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "object": (["min_side", "max_side", "total_pixels"], {"default": "min_side"}),
                "comparison": ([">", ">=", "=", "<", "<="], {"default": ">"}),
                "value": ("INT", {"default": 256})
            }
        }

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "execute"

    CATEGORY = "12utils/image"

    def execute(self, image, object, comparison, value):
        # Assuming image is a numpy array with shape (height, width, channels)
        height, width, _ = image.shape

        if object == "min_side":
            computed_value = min(height, width)
        elif object == "max_side":
            computed_value = max(height, width)
        elif object == "total_pixels":
            computed_value = height * width

        if comparison == ">":
            result = computed_value > value
        elif comparison == ">=":
            result = computed_value >= value
        elif comparison == "=":
            result = computed_value == value
        elif comparison == "<":
            result = computed_value < value
        elif comparison == "<=":
            result = computed_value <= value

        return (result,)

# Example usage:
# result = VerifyImageSide().execute(image_array, "min_side", ">", 256)
# print(result)

NODE_CLASS_MAPPINGS = {
    "VerifyImageSide": VerifyImageSide, # 验证图片边长
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VerifyImageSide": "Verify Image Side", # 验证图片边长
}