"""
ComfyUI-SmartSize
A simple but essential custom node for ComfyUI that automatically detects image dimensions
and snaps them to the nearest multiple of 16. This is critical for Flux and SDXL workflows
to prevent EinopsError (shape mismatch) and ensure high-quality generation.
"""


class SmartSize:
    """
    A ComfyUI custom node that snaps image dimensions to the nearest multiple of 16.
    This prevents EinopsError in Flux and SDXL workflows.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {
                    "default": 1024,
                    "min": 64,
                    "max": 8192,
                    "step": 1,
                    "display": "number"
                }),
                "height": ("INT", {
                    "default": 1024,
                    "min": 64,
                    "max": 8192,
                    "step": 1,
                    "display": "number"
                }),
            },
        }
    
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "snap_to_multiple"
    CATEGORY = "image/dimensions"
    
    def snap_to_multiple(self, width, height):
        """
        Snap width and height to the nearest multiple of 16.
        
        Args:
            width: Input width
            height: Input height
            
        Returns:
            Tuple of (snapped_width, snapped_height)
        """
        # Round to nearest multiple of 16
        snapped_width = round(width / 16) * 16
        snapped_height = round(height / 16) * 16
        
        # Ensure minimum of 64 (4 * 16)
        snapped_width = max(64, snapped_width)
        snapped_height = max(64, snapped_height)
        
        return (snapped_width, snapped_height)


# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "SmartSize": SmartSize
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SmartSize": "Smart Size (Snap to 16)"
}
