'''
author:
    Stability-AI/stability-ComfyUI-nodes

overview:
    This node extracts and saves LoRA (Low-Rank Adaptation) weights from the differences between a model and a control net. 
    It performs singular value decomposition (SVD) on the weight differences, clamps the values, and reshapes them based on the convolutional nature of the weights. 
    The LoRA weights are then saved to a safetensors file.

input:
    model(MODEL): The base model.
    control_net(CONTROL_NET): The control net.
    filename_prefix(str): The prefix for the output file name.
    rank(int): The rank for the LoRA decomposition. Default is 64.

output:
    None

# zh
功能:
    此节点从模型和控制网络之间的差异中提取并保存LoRA（低秩适应）权重。它对权重差异执行奇异值分解（SVD），对值进行钳制，并根据权重的卷积性质重塑它们。然后将LoRA权重保存到safetensors文件中。

输入:
    model(MODEL): 基础模型。
    control_net(CONTROL_NET): 控制网络。
    filename_prefix(str): 输出文件名的前缀。
    rank(int): LoRA分解的秩。默认为64。

输出:
    无
'''
from ...thirdparty.stability_ComfyUI_nodes.control_lora_create import *