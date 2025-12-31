"""
ComfyUI-SmartSize
A custom node for ComfyUI that automatically detects and adjusts image dimensions.
"""

from .smart_size_node import SmartImageSize

NODE_CLASS_MAPPINGS = {
    "SmartImageSize": SmartImageSize
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SmartImageSize": "Smart Image Size (Flux/SDXL)"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
