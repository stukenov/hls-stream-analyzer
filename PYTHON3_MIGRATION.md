# Python 3.10 Migration Guide

This document describes the changes made to migrate the HLS Analyzer project from Python 2.x to Python 3.10+.

## Changes Made

### 1. Print Statements
- **Before**: `print "text"` (Python 2 syntax)
- **After**: `print("text")` (Python 3 syntax)
- **Files affected**: `hls-analyzer.py`

### 2. Division Operators
- **Before**: `a / b` (floating-point division in Python 2, but could cause issues in Python 3)
- **After**: `a // b` (explicit integer division)
- **Files affected**: 
  - `bitreader.py` - `setPosition()`, `skipBits()`, `readSignedExpGolombCodedInt()`
  - `parsers/adtsreader.py` - `_parseAACHeader()`
  - `parsers/pesreader.py` - `_ptsToTimeUs()`

### 3. Dictionary Methods
- **Before**: `dict.iteritems()` (Python 2)
- **After**: `dict.items()` (Python 3)
- **Files affected**: 
  - `hls-analyzer.py` - `analyze_variants_frame_alignment()`
  - `ts_segment.py` - `getTrack()`

### 4. Import Statements
- **Before**: `import urllib2` (Python 2)
- **After**: `from urllib.request import urlopen, build_opener` (Python 3)
- **Files affected**: `hls-analyzer.py`

### 5. Print with end parameter
- **Before**: `print "text",` (trailing comma for no newline in Python 2)
- **After**: `print("text", end="")` (explicit end parameter in Python 3)
- **Files affected**: `hls-analyzer.py` - `analyzeFrames()`

## Files Modified

1. **hls-analyzer.py** - Main script with most Python 2 compatibility fixes
2. **bitreader.py** - Fixed integer division operations
3. **ts_segment.py** - Updated dictionary iteration method
4. **parsers/adtsreader.py** - Fixed integer division
5. **parsers/pesreader.py** - Fixed integer division
6. **requirements.txt** - Updated dependency version
7. **setup.py** - Added Python 3 classifiers and requirements
8. **README.md** - Added Python 3.10 compatibility information

## Testing

The project has been tested with:
- Python 3.10+
- All Python files compile without syntax errors
- All modules can be imported successfully
- Basic functionality works with HLS streams

## Compatibility

- **Python 3.7+**: Fully supported
- **Python 3.10+**: Tested and recommended
- **Python 2.x**: No longer supported

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Or install the package
python setup.py install
```

## Usage

```bash
python hls-analyzer.py <HLS_STREAM_URL>
```

## Notes

- The project maintains backward compatibility with Python 3.7+
- All functionality from the original Python 2.x version is preserved
- The m3u8 library included in the project has been updated for Python 3 compatibility
- No breaking changes to the API or command-line interface
