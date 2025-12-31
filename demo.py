"""
Demo script to showcase SmartSize functionality
"""

from __init__ import SmartSize


def demo():
    print("=" * 60)
    print("ComfyUI-SmartSize Demonstration")
    print("=" * 60)
    print("\nThis node snaps dimensions to the nearest multiple of 16")
    print("to prevent EinopsError in Flux and SDXL workflows.\n")
    
    node = SmartSize()
    
    test_cases = [
        (1024, 1024, "Standard SDXL square"),
        (1000, 750, "Custom dimensions"),
        (1920, 1080, "Full HD"),
        (2560, 1440, "2K resolution"),
        (3840, 2160, "4K resolution"),
        (768, 512, "Landscape"),
        (512, 768, "Portrait"),
        (100, 100, "Small image"),
        (50, 50, "Below minimum (will snap to 64)"),
    ]
    
    print(f"{'Input':<20} {'→':<5} {'Output':<20} {'Description':<30}")
    print("-" * 80)
    
    for width, height, description in test_cases:
        snapped_width, snapped_height = node.snap_to_multiple(width, height)
        changed = " ✓" if (width != snapped_width or height != snapped_height) else ""
        print(f"{width}×{height:<15} → {snapped_width}×{snapped_height:<15} {description:<30}{changed}")
    
    print("\n" + "=" * 60)
    print("Common Flux/SDXL Resolutions (already multiples of 16):")
    print("=" * 60)
    
    common_resolutions = [
        (1024, 1024, "1:1 square"),
        (1152, 896, "9:7 landscape"),
        (896, 1152, "7:9 portrait"),
        (1216, 832, "19:13 landscape"),
        (832, 1216, "13:19 portrait"),
        (1344, 768, "7:4 wide"),
        (768, 1344, "4:7 tall"),
        (1536, 640, "12:5 ultrawide"),
    ]
    
    for width, height, ratio in common_resolutions:
        print(f"  {width}×{height:<10} ({ratio})")
    
    print("\n✅ All these resolutions pass through unchanged!")
    print("=" * 60)


if __name__ == "__main__":
    demo()
