#!/usr/bin/env python3
"""Script to run API tests with different reporting options"""

import subprocess
import sys
import os

def run_tests():
    """Run API tests with selected reporting"""
    print("Running API tests...")
    
    # Basic test run
    result = subprocess.run([
        "pytest", 
        "src/api/tests/",
        "-v",
        "--tb=short"
    ], cwd=os.path.dirname(os.path.abspath(__file__)))
    
    if result.returncode == 0:
        print("✅ All API tests passed!")
    else:
        print("❌ Some API tests failed!")
    
    return result.returncode

if __name__ == "__main__":
    sys.exit(run_tests())