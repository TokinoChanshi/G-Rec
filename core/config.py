import os
from pathlib import Path
from dotenv import load_dotenv

# --- Path Configuration ---
CORE_DIR = Path(__file__).parent.absolute()
PROJECT_ROOT = CORE_DIR.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
LOGS_DIR = PROJECT_ROOT / "logs"
OUTPUT_DIR = PROJECT_ROOT / "output"
SKILL_INDEX = CORE_DIR / "SKILL_INDEX.md"
TASK_QUEUE = CORE_DIR / "TASK_QUEUE.md"
MISTAKE_BOOK = CORE_DIR / "MISTAKE_BOOK.md"
MEMORY = CORE_DIR / "MEMORY.md"

# --- Load Environment Variables ---
# Try loading from .env, fallback to .env.template (for defaults) is logic we could add,
# but usually we just want to load .env if it exists.
ENV_PATH = PROJECT_ROOT / ".env"
load_dotenv(ENV_PATH)

# --- Global Constants ---
# Colors for Console Output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Platform Check
IS_WINDOWS = os.name == 'nt'

# Encoding Force
def force_utf8():
    import sys
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

# Ensure critical dirs exist
def ensure_dirs():
    LOGS_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

# Run on import
force_utf8()
ensure_dirs()
