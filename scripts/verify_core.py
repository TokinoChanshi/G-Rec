import sys
import os
from pathlib import Path

# Add core directory to path
core_path = Path("G-Rec/core").absolute()
sys.path.append(str(core_path))

print(f"Testing imports from: {core_path}")

try:
    import config
    print("✅ config.py imported")
    
    import manager
    print("✅ manager.py imported")
    
    import task_manager
    print("✅ task_manager.py imported")
    
    import prevention
    print("✅ prevention.py imported")
    
    import health
    print("✅ health.py imported")
    
    print("\n🎉 ALL CORE MODULES PASSED IMPORT TEST")
except Exception as e:
    print(f"\n❌ IMPORT FAILED: {e}")
    sys.exit(1)
