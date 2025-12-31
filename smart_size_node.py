"""
ComfyUI-SmartSize: A custom node for automatically detecting and adjusting image dimensions
to the nearest multiple of 16, essential for Flux and SDXL workflows.
"""

class SmartImageSize:
    """
    A ComfyUI custom node that detects image dimensions and snaps them to the nearest
    multiple of 16 to prevent EinopsError and ensure compatibility with Flux/SDXL models.
    
    This node takes an IMAGE input from ComfyUI (typically from a Load Image node) and
    outputs adjusted width and height values that are guaranteed to be multiples of 16.
    These outputs can be connected to Empty Latent, ModelSamplingFlux, or ImageScale nodes.
    
    Usage:
        1. Connect a Load Image node to the image input
        2. Connect the width/height outputs to target nodes
        3. Convert target node widgets to inputs if needed (right-click -> Convert Widget to Input)
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
            
        Raises:
            ValueError: If the image tensor doesn't have the expected 4D shape
        """
        # ComfyUI image tensors are in format: (batch, height, width, channels)
        # Validate the tensor shape before unpacking
        if len(image.shape) != 4:
            raise ValueError(
                f"Expected 4D image tensor (batch, height, width, channels), "
                f"but got shape {image.shape}"
            )
        
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
            value: The value to snap (must be non-negative)
            multiple: The multiple to snap to (must be positive)
            
        Returns:
            The value snapped to the nearest multiple as an integer
            
        Raises:
            ValueError: If multiple is zero or negative, or if value is negative
        """
        if multiple <= 0:
            raise ValueError(f"Multiple must be positive, got {multiple}")
        if value < 0:
            raise ValueError(f"Value must be non-negative, got {value}")
        
        return int(round(value / multiple) * multiple)
