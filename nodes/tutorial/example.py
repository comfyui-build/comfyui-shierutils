import folder_paths
import comfy.samplers
import comfy.model_management
import torch
import random

__all__ = [
    "a1",
    "a2",
    "a3",
    "a4",
]


class a1:
    def __init__(self):
        pass

    CATEGORY = "tutorial/example"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "左边的输入": ("STRING", {"forceInput": True}),
                "参数：整数": ("INT", {
                    "default": 20,
                    "min": 1,
                    "max": 10000,
                    "step": 2,
                    "display": "number"}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("1整数",)

    FUNCTION = "test"

    def test(self):
        pass

class a2:
    def __init__(self):
        pass

    CATEGORY = "12utils/tutorial/example"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pipe": ("PIPE_LINE",),
                "参数：整数": ("INT", {
                    "default": 20,
                    "min": 1,
                    "max": 10000,
                    "step": 2,
                    "display": "number"}),
                "参数：浮点数": ("FLOAT", {
                    "default": 1.0,
                    "min": -10.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001,
                    "display": "slider"}),
                "参数：字符串": ("STRING", {
                    "default": "啊啊啊啊啊啊",
                    "multiline": True}),
                "参数：布尔值": ("BOOLEAN", {
                    "default": True}),
                "下拉选择框": (["None"] + ["enable", "disable"],),
            },
            "optional": {
                "model": ("MODEL",),
                "vae": ("VAE",),
                "clip": ("CLIP",),
                "latent": ("LATENT",),
                "image": ("IMAGE",),
                "pos": ("CONDITIONING",),
                "neg": ("CONDITIONING",),
                "xyPlot": ("XYPLOT",),
            },
            "hidden": {"my_unique_id": "UNIQUE_ID"},
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("PIPE_LINE","MODEL","VAE","CLIP","LATENT","IMAGE","CONDITIONING","CONDITIONING","INT", "FLOAT", "STRING",)
    RETURN_NAMES = ("0pepe","1model","2vae","3clip","4latent","5image","6pos","7neg","8整数","9浮点数","10字符串",)

    FUNCTION = "test"

    def test(self):
        pass

class a3:
    def __init__(self):
        pass

    CATEGORY = "tutorial/example"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "获取本地checkpoint": (["None"] + folder_paths.get_filename_list("checkpoints"),),
                "获取本地vae": (["None"] + folder_paths.get_filename_list("vae"),),
                "获取本地lora": (["None"] + folder_paths.get_filename_list("loras"),),
                "获取本地sampler": (comfy.samplers.KSampler.SAMPLERS,),
                "获取本地scheduler": (comfy.samplers.KSampler.SCHEDULERS,),
                "seed": ("INT", {"default": 123, "min": 0, "max": 0xffffffffffffffff, "step": 1}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("1整数",)

    FUNCTION = "test"

    def test(self):
        comfy.model_management.unload_all_models()
        device = comfy.model_management.get_torch_device()
        seed = '123'
        torch.manual_seed(seed)
        pass

class a4:
    def __init__(self):
        pass

    CATEGORY = "tutorial/example"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width": ("INT", {"default": 256, "min": 128, "max": 2048, "step": 128}),
                "height": ("INT", {"default": 256, "min": 128, "max": 2048, "step": 128}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image(torch.Tensor)",)

    FUNCTION = "test"

    def test(self, width, height):
        comfy.model_management.unload_all_models()
        seed = random.randint(0, 0xffffffffffffffff)
        torch.manual_seed(seed)
        noise = torch.randn((1, 3, width, height), device="cuda")
        tensor = noise.permute(0, 2, 3, 1).cpu()
        return (tensor,)