"""
ComfyUI-SmartSize: A custom node for automatically detecting and adjusting image dimensions
to the nearest multiple of 16, essential for Flux and SDXL workflows.
"""

class SmartImageSize:
    """
    A ComfyUI custom node that detects image dimensions and snaps them to the nearest
    multiple of 16 to prevent EinopsError and ensure compatibility with Flux/SDXL models.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }
    
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "calculate_size"
    CATEGORY = "image/size"
    
    def calculate_size(self, image):
        """
        Calculate width and height from input image and snap to nearest multiple of 16.
        
        Args:
            image: Input image tensor (batch, height, width, channels)
            
        Returns:
            Tuple of (width, height) snapped to nearest multiple of 16
        """
        # ComfyUI image tensors are in format: (batch, height, width, channels)
        # Get the dimensions from the tensor shape
        _, height, width, _ = image.shape
        
        # Snap to nearest multiple of 16
        snapped_width = self._snap_to_multiple(width, 16)
        snapped_height = self._snap_to_multiple(height, 16)
        
        return (snapped_width, snapped_height)
    
    def _snap_to_multiple(self, value, multiple):
        """
        Snap a value to the nearest multiple.
        
        Args:
            value: The value to snap
            multiple: The multiple to snap to
            
        Returns:
            The value snapped to the nearest multiple
        """
        return round(value / multiple) * multiple
