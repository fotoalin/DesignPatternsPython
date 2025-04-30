"""
Configure pytest to properly handle imports between packages in the BuilderPattern module.
This file is automatically recognized by pytest and helps with import resolution.
"""

import sys
import os
from pathlib import Path

# Add the BuilderPattern directory to sys.path
module_path = Path(__file__).resolve().parent
sys.path.insert(0, str(module_path))