import torch

class GetImageSize_Custom:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",)}}
    
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_size"
    CATEGORY = "SmartSize"

    def get_size(self, image):
        # image is [Batch, Height, Width, Channels]
        _, h, w, _ = image.shape
        # Ensure multiple of 16 for Flux/SDXL to avoid shape errors
        w = (w // 16) * 16
        h = (h // 16) * 16
        return (w, h)

NODE_CLASS_MAPPINGS = {
    "GetImageSize_Custom": GetImageSize_Custom
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GetImageSize_Custom": "Smart Image Size (Flux/SDXL)"
}
