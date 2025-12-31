# ComfyUI-SmartSize

A simple but essential custom node for ComfyUI that automatically detects image dimensions and snaps them to the nearest multiple of 16. This is critical for **Flux** and **SDXL** workflows to prevent `EinopsError` (shape mismatch) and ensure high-quality generation.

## 🎯 Why SmartSize?

When working with modern AI image generation models like Flux and SDXL, you may encounter errors like:
```
EinopsError: Error while processing rearrange-reduction pattern "b c (h ph) (w pw) -> b (h w) (c ph pw)"
```

This happens because these models require image dimensions to be multiples of 16 (or 64 for some configurations). SmartSize automatically handles this for you by:

- 📏 Snapping any input dimensions to the nearest multiple of 16
- 🛡️ Preventing shape mismatch errors in Flux and SDXL workflows
- ⚡ Ensuring optimal performance and quality
- ✅ Supporting a wide range of resolutions (64-8192px)

## 🚀 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "SmartSize" in the manager
3. Click Install

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/xiujiang1987/ComfyUI-SmartSize.git
   ```
3. Restart ComfyUI

## 📖 Usage

### In ComfyUI Workflow

1. Add the **Smart Size (Snap to 16)** node to your workflow
2. Connect or input your desired width and height
3. The node outputs the snapped dimensions that are safe to use with Flux/SDXL

### Example

**Input:**
- Width: 1000
- Height: 750

**Output:**
- Width: 992 (nearest multiple of 16)
- Height: 752 (nearest multiple of 16)

### Node Details

**Inputs:**
- `width` (INT): Desired width (64-8192, default: 1024)
- `height` (INT): Desired height (64-8192, default: 1024)

**Outputs:**
- `width` (INT): Snapped width (multiple of 16)
- `height` (INT): Snapped height (multiple of 16)

## 🔧 How It Works

The node uses a simple but effective algorithm:

```python
snapped_width = round(width / 16) * 16
snapped_height = round(height / 16) * 16
```

This ensures:
- Values are rounded to the **nearest** multiple of 16 (not just floor or ceil)
- Minimum dimensions of 64x64 are enforced
- All outputs are compatible with Flux, SDXL, and similar models

## 💡 Common Use Cases

### Flux Workflows
Connect SmartSize before your Flux model nodes to ensure compatible dimensions.

### SDXL Workflows  
Use SmartSize to prepare dimensions for SDXL's VAE encoding/decoding stages.

### ControlNet & LoRA
Prevent dimension mismatches when using ControlNet or LoRA with base models.

### Image Resizing
Ensure any custom resolution stays compatible with your model pipeline.

## 🌟 Popular SDXL/Flux Resolutions

The following resolutions are already multiples of 16 and will pass through unchanged:
- 1024×1024 (1:1 square)
- 1152×896 (9:7 landscape)
- 896×1152 (7:9 portrait)
- 1216×832 (19:13 landscape)
- 832×1216 (13:19 portrait)
- 1344×768 (7:4 wide)
- 768×1344 (4:7 tall)
- 1536×640 (12:5 ultrawide)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Credits

Created to make Flux and SDXL workflows more reliable and user-friendly in ComfyUI.