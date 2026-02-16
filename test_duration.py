#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify duration calculation fixes
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported"""
    try:
        from bitreader import BitReader
        print("✓ bitreader imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import bitreader: {e}")
        return False
    
    try:
        from ts_segment import TSSegmentParser
        print("✓ ts_segment imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import ts_segment: {e}")
        return False
    
    try:
        from parsers.payloadreader import PayloadReader
        print("✓ payloadreader imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import payloadreader: {e}")
        return False
    
    return True

def test_duration_calculation():
    """Test duration calculation logic"""
    from parsers.payloadreader import PayloadReader
    
    # Create a mock payload reader
    class MockPayloadReader(PayloadReader):
        def __init__(self):
            super().__init__()
            self._firstPts = 1000000  # 1 second in microseconds
            self._lastPts = 7000000   # 7 seconds in microseconds
        
        def getFirstPTS(self):
            return self._firstPts
        
        def getLastPTS(self):
            return self._lastPts
    
    reader = MockPayloadReader()
    duration = reader.getDuration()
    expected_duration = 6000000  # 6 seconds in microseconds
    
    print(f"Test duration calculation:")
    print(f"  First PTS: {reader.getFirstPTS()} μs ({reader.getFirstPTS()/1000000:.2f}s)")
    print(f"  Last PTS: {reader.getLastPTS()} μs ({reader.getLastPTS()/1000000:.2f}s)")
    print(f"  Calculated duration: {duration} μs ({duration/1000000:.2f}s)")
    print(f"  Expected duration: {expected_duration} μs ({expected_duration/1000000:.2f}s)")
    
    if duration == expected_duration:
        print("  ✓ Duration calculation is correct")
        return True
    else:
        print("  ✗ Duration calculation is incorrect")
        return False

def test_bitreader_division():
    """Test that bitreader division operations work correctly"""
    from bitreader import BitReader
    
    # Create test data
    test_data = bytearray([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07])
    reader = BitReader(test_data)
    
    # Test setPosition with division
    reader.setPosition(16)  # 16 bits = 2 bytes
    position = reader.getPosition()
    expected_position = 16
    
    print(f"Test bitreader division:")
    print(f"  Set position to 16 bits")
    print(f"  Byte offset: {reader.byteOffset}")
    print(f"  Bit offset: {reader.bitOffset}")
    print(f"  Calculated position: {position}")
    print(f"  Expected position: {expected_position}")
    
    if position == expected_position:
        print("  ✓ Bitreader division works correctly")
        return True
    else:
        print("  ✗ Bitreader division has issues")
        return False

if __name__ == "__main__":
    print("Testing HLS Analyzer Python 3.10 compatibility fixes")
    print("=" * 60)
    
    print("\n1. Testing imports...")
    imports_ok = test_imports()
    
    print("\n2. Testing duration calculation...")
    duration_ok = test_duration_calculation()
    
    print("\n3. Testing bitreader division...")
    bitreader_ok = test_bitreader_division()
    
    print("\n" + "=" * 60)
    if imports_ok and duration_ok and bitreader_ok:
        print("✓ All tests passed! Duration calculation fixes are working.")
    else:
        print("✗ Some tests failed. Please check the errors above.")
    
    sys.exit(0 if (imports_ok and duration_ok and bitreader_ok) else 1)
