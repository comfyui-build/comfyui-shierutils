'''
author:
    Stability-AI/stability-ComfyUI-nodes

overview:
    This node performs a color blending operation on two input images: a black and white layer and a color layer.
    The operation involves converting the color layer to the LAB color space, replacing its luminance channel with the luminance channel of the black and white layer, and then converting the result back to the BGR color space.
    This process effectively blends the color information of the color layer with the luminance information of the black and white layer.

input:
    bw_layer(torch.Tensor): Black and white image.
    color_layer(torch.Tensor): Color image.

output:
    torch.Tensor: Image after blending the color layer and black and white layer.

# zh
功能:
    此节点对两个输入图像执行颜色混合操作:一个黑白图层和一个彩色图层。
    操作包括将彩色图层转换为LAB色彩空间，将其亮度通道替换为黑白图层的亮度通道，然后将结果转换回BGR色彩空间。
    此过程有效地将彩色图层的颜色信息与黑白图层的亮度信息混合在一起。

输入:
    bw_layer(torch.Tensor): 黑白图像。
    color_layer(torch.Tensor): 彩色图像。

输出:
    torch.Tensor: 混合彩色图层和黑白图层后的图像。
'''

# Color blend node by Yam Levi
# Property of Stability AI
import cv2
import numpy as np
from PIL import Image
import torch
import comfy.utils

def color_blend(bw_layer,color_layer):
    # Convert the color layer to LAB color space
    color_lab = cv2.cvtColor(color_layer, cv2.COLOR_BGR2Lab)
    # Convert the black and white layer to grayscale
    bw_layer_gray = cv2.cvtColor(bw_layer, cv2.COLOR_BGR2GRAY)
    # Replace the luminosity (L) channel in the color image with the black and white luminosity
    _, color_a, color_b = cv2.split(color_lab)
    blended_lab = cv2.merge((bw_layer_gray, color_a, color_b))
    # Convert the blended LAB image back to BGR color space
    blended_result = cv2.cvtColor(blended_lab, cv2.COLOR_Lab2BGR)
    return blended_result

class BwColorBlend:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "bw_layer": ("IMAGE",),
                "color_layer": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "color_blending_mode"

    CATEGORY = "image/postprocessing"

    def color_blending_mode(self, bw_layer, color_layer):
        if bw_layer.shape[0] < color_layer.shape[0]:
            bw_layer = bw_layer.repeat(color_layer.shape[0], 1, 1, 1)[:color_layer.shape[0]]
        if bw_layer.shape[0] > color_layer.shape[0]:
            color_layer = color_layer.repeat(bw_layer.shape[0], 1, 1, 1)[:bw_layer.shape[0]]

        batch_size, height, width, _ = bw_layer.shape
        tensor_output = torch.empty_like(bw_layer)

        image1 = bw_layer.cpu()
        image2 = color_layer.cpu()
        if image1.shape != image2.shape:
            #print(image1.shape)
            #print(image2.shape)
            image2 = image2.permute(0, 3, 1, 2)
            image2 = comfy.utils.common_upscale(image2, image1.shape[2], image1.shape[1], upscale_method='bicubic', crop='center')
            image2 = image2.permute(0, 2, 3, 1)
        image1  = (image1 * 255).to(torch.uint8).numpy()
        image2 = (image2 * 255).to(torch.uint8).numpy()

        for i in range(batch_size):
            blend = color_blend(image1[i],image2[i])
            blend = np.stack([blend])
            tensor_output[i:i+1] = (torch.from_numpy(blend.transpose(0, 3, 1, 2))/255.0).permute(0, 2, 3, 1)

        return (tensor_output,)


NODE_CLASS_MAPPINGS = {
    "BwColorBlend": BwColorBlend
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "BwColorBlend": "Bw Color Blend"
}
