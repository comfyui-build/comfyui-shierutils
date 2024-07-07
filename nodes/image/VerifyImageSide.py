'''
author:
    shiertier

overview:
    This node verifies the dimensions of an input image based on specified criteria. It compares the minimum side length, maximum side length, or total number of pixels of the image against a given value using a selected comparison operator.

input:
    IMAGE(torch.Tensor): Input image tensor.
    compare_object(dropdown): Criteria to compare (min_side, max_side, total_pixels). Default is min_side.
    comparison(dropdown): Comparison operator (>, >=, =, <, <=). Default is >.
    value(int): Value to compare against. Default is 256.

output:
    BOOL: True if the comparison condition is met, otherwise False.

# zh
功能:
    此节点根据指定条件验证输入图像的尺寸。它将图像的最小边长、最大边长或总像素数与给定值使用选定的比较运算符进行比较。

输入:
    IMAGE(torch.Tensor): 输入图像张量。
    compare_object(下拉菜单): 比较标准（最小边长，最大边长，总像素数）。默认是最小边长。
    comparison(下拉菜单): 比较运算符（>, >=, =, <, <=）。默认是>。
    value(int): 比较的值。默认是256。

输出:
    BOOL: 如果比较条件满足则为真，否则为假。
'''

import numpy as np
import torch

class VerifyImageSide:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "IMAGE": ("IMAGE",),
                "compare_object": (["min_side", "max_side", "total_pixels"], {"default": "min_side"}),
                "comparison": ([">", ">=", "=", "<", "<="], {"default": ">"}),
                "value": ("INT", {"default": 256})
            }
        }

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "execute"

    CATEGORY = "image"

    def execute(self, IMAGE, compare_object, comparison, value):
        # Check the type of IMAGE and handle accordingly
        if isinstance(IMAGE, np.ndarray):
            image = IMAGE
        elif isinstance(IMAGE, torch.Tensor):
            image = IMAGE.numpy()
        elif isinstance(IMAGE, torch.Size):
            image = torch.tensor(IMAGE).numpy()
        else:
            raise TypeError("Unsupported image type: {}".format(type(IMAGE)))

        # Assuming image is a numpy array with shape (height, width, channels)
        if len(image.shape) == 4:
            batch_size, height, width, channels = image.shape
            if batch_size != 1:
                raise ValueError(f'No more than 1 image allowed: {batch_size}')
            # Extract the single image from the batch
            image = image[0]
        elif len(image.shape) == 3:
            height, width, channels = image.shape
        elif len(image.shape) == 2:
            height, width = image.shape
            channels = 1  # Assuming grayscale images have one channel
        else:
            raise ValueError("Unexpected image shape: {}".format(image.shape))

        if compare_object == "min_side":
            computed_value = min(height, width)
        elif compare_object == "max_side":
            computed_value = max(height, width)
        elif compare_object == "total_pixels":
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
        print(int(result))
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