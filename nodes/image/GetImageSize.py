'''
author:
    Stability-AI/stability-ComfyUI-nodes

overview:
    This node retrieves the dimensions (width and height) of an input image.

input:
    image(torch.Tensor): Input image tensor.

output:
    INT: Width of the image.
    INT: Height of the image.

# zh
功能:
    此节点获取输入图像的尺寸（宽度和高度）。

输入:
    image(torch.Tensor): 输入图像张量。

输出:
    INT: 图像的宽度。
    INT: 图像的高度。
'''


class GetImageSize:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")

    FUNCTION = "get_size"

    CATEGORY = "stability/image"

    def get_size(self, image):
        _, height, width, _ = image.shape
        return (width, height)

NODE_CLASS_MAPPINGS = {
    "GetImageSize": GetImageSize
}

NODE_DISPLAY_NAME_MAPPINGS = {
}
