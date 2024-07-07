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

from ...thirdparty.stability_ComfyUI_nodes.bw_color_blend import *