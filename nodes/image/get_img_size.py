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

from ...thirdparty.stability_ComfyUI_nodes.get_img_size import *