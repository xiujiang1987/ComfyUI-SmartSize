"""
Unit tests for SmartSize node
"""

import sys
import os

# Add the current directory to the path so we can import __init__
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from __init__ import SmartSize


def test_exact_multiples():
    """Test that exact multiples of 16 pass through unchanged"""
    node = SmartSize()
    
    # Test standard resolutions
    assert node.snap_to_multiple(1024, 1024) == (1024, 1024)
    assert node.snap_to_multiple(512, 768) == (512, 768)
    assert node.snap_to_multiple(1152, 896) == (1152, 896)
    print("✓ Exact multiples test passed")


def test_rounding_down():
    """Test that values round to nearest multiple of 16"""
    node = SmartSize()
    
    # 1000/16=62.5 rounds to 62 -> 992, 750/16=46.875 rounds to 47 -> 752
    assert node.snap_to_multiple(1000, 750) == (992, 752)
    # 513/16=32.0625 rounds to 32 -> 512, 769/16=48.0625 rounds to 48 -> 768
    assert node.snap_to_multiple(513, 769) == (512, 768)
    print("✓ Rounding test passed")


def test_rounding_up():
    """Test that values round up to nearest multiple of 16"""
    node = SmartSize()
    
    # 520/16=32.5 rounds to 32 -> 512, 776/16=48.5 rounds to 48 -> 768
    assert node.snap_to_multiple(520, 776) == (512, 768)
    # 1030/16=64.375 rounds to 64 -> 1024
    assert node.snap_to_multiple(1030, 1030) == (1024, 1024)
    print("✓ Rounding up test passed")


def test_minimum_dimensions():
    """Test that minimum dimension of 64 is enforced"""
    node = SmartSize()
    
    # Should enforce minimum
    assert node.snap_to_multiple(32, 32) == (64, 64)
    assert node.snap_to_multiple(0, 0) == (64, 64)
    assert node.snap_to_multiple(50, 100) == (64, 96)
    print("✓ Minimum dimensions test passed")


def test_edge_cases():
    """Test edge cases"""
    node = SmartSize()
    
    # 520/16=32.5 rounds to 32 (nearest even) -> 512
    assert node.snap_to_multiple(520, 520) == (512, 512)
    # 1016/16=63.5 rounds to 64 (nearest even) -> 1024
    assert node.snap_to_multiple(1016, 1016) == (1024, 1024)
    
    # Test large dimensions
    assert node.snap_to_multiple(8000, 8000) == (8000, 8000)
    assert node.snap_to_multiple(8191, 8191) == (8192, 8192)
    print("✓ Edge cases test passed")


def test_flux_sdxl_common_resolutions():
    """Test common Flux and SDXL resolutions"""
    node = SmartSize()
    
    # Common SDXL resolutions (should all be multiples of 16)
    common_resolutions = [
        (1024, 1024),  # 1:1 square
        (1152, 896),   # 9:7 landscape
        (896, 1152),   # 7:9 portrait
        (1216, 832),   # 19:13 landscape
        (832, 1216),   # 13:19 portrait
        (1344, 768),   # 7:4 wide
        (768, 1344),   # 4:7 tall
        (1536, 640),   # 12:5 ultrawide
    ]
    
    for width, height in common_resolutions:
        result = node.snap_to_multiple(width, height)
        assert result == (width, height), f"Failed for {width}x{height}: got {result}"
    
    print("✓ Flux/SDXL common resolutions test passed")


def test_node_structure():
    """Test that the node has the required ComfyUI structure"""
    # Check INPUT_TYPES
    input_types = SmartSize.INPUT_TYPES()
    assert "required" in input_types
    assert "width" in input_types["required"]
    assert "height" in input_types["required"]
    
    # Check return types
    assert SmartSize.RETURN_TYPES == ("INT", "INT")
    assert SmartSize.RETURN_NAMES == ("width", "height")
    assert SmartSize.FUNCTION == "snap_to_multiple"
    assert SmartSize.CATEGORY == "image/dimensions"
    
    print("✓ Node structure test passed")


if __name__ == "__main__":
    print("Running SmartSize node tests...\n")
    
    test_exact_multiples()
    test_rounding_down()
    test_rounding_up()
    test_minimum_dimensions()
    test_edge_cases()
    test_flux_sdxl_common_resolutions()
    test_node_structure()
    
    print("\n✅ All tests passed!")
