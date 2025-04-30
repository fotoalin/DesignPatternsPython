"""
Configure pytest to properly handle imports specifically for email_templates tests.
"""

import sys
import os
from pathlib import Path

# Add the email_templates directory to sys.path
module_path = Path(__file__).resolve().parent
sys.path.insert(0, str(module_path))

# Add the BuilderPattern directory to sys.path for sibling package imports
parent_path = module_path.parent
sys.path.insert(0, str(parent_path))