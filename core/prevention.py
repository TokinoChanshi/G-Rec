#!/usr/bin/env python3
"""
G-Rec Error Prevention Module (The Shield)
Proactive risk analysis and pre-flight checks before execution.
"""
import sys
import re
from pathlib import Path

try:
    from .config import MISTAKE_BOOK, force_utf8, Colors
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent))
    from config import MISTAKE_BOOK, force_utf8, Colors

# Initialize
force_utf8()


# 🛑 Hardcoded High-Risk Patterns (The "Red Lines")
CRITICAL_RISKS = [
    (r"rm\s+-rf\s+[/|\\]", "ROOT_DELETION_ATTEMPT"),
    (r"del\s+.*\*.*", "WILDCARD_DELETION_RISK"),
    (r"format\s+[c-z]:", "DRIVE_FORMAT_ATTEMPT"),
    (r"pip\s+uninstall\s+python", "ENV_DESTRUCTION_RISK"),
    (r"rmdir\s+/s\s+/q\s+[c-z]:\\", "DRIVE_WIPE_ATTEMPT"),
    (r"git\s+reset\s+--hard", "GIT_HISTORY_DESTRUCTION"),
    (r"echo\s+.*\s+>\s+.*(System32|Windows)", "SYSTEM_FILE_OVERWRITE")
]

def load_mistake_patterns():
    """Extracts 'Issue' -> 'Solution' pairs from MISTAKE_BOOK.md"""
    patterns = []
    if not MISTAKE_BOOK.exists():
        return patterns
    
    with open(MISTAKE_BOOK, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract Issue and Solution blocks
    # Looking for "- **Issue**: ... \n ... - **Solution**: ..."
    entries = content.split("- **Issue**:")
    for entry in entries[1:]:
        issue_match = re.search(r"^\s*(.*)", entry)
        solution_match = re.search(r"- \*\*Solution\*\*:\s*(.*)", entry)
        
        if issue_match and solution_match:
            patterns.append({
                "issue": issue_match.group(1).strip(),
                "solution": solution_match.group(1).strip()
            })
    return patterns

def scan_command(command):
    """Scans a proposed command/action for risks"""
    warnings = []
    
    # 1. Check Hardcoded Risks
    for pattern, risk_name in CRITICAL_RISKS:
        if re.search(pattern, command, re.IGNORECASE):
            warnings.append(f"🛑 CRITICAL: {risk_name} detected in '{command}'")

    # 2. Check Path Safety (Basic Sandboxing)
    # Block writing to C:\Windows or C:\Program Files
    if "C:\\Windows" in command or "C:\\Program Files" in command:
        if ">" in command or "rm" in command or "del" in command:
             warnings.append(f"🛑 SYSTEM PROTECT: Access to System Folders blocked.")
    
    return warnings

def scan_intent(intent):
    """Scans user intent against Mistake Book"""
    warnings = []
    mistakes = load_mistake_patterns()
    
    intent_lower = intent.lower()
    
    for item in mistakes:
        # Simple keyword overlap check
        issue_keywords = set(item['issue'].lower().split())
        intent_keywords = set(intent_lower.split())
        
        # Filter out common stop words
        stop_words = {"the", "a", "is", "in", "to", "my", "it", "not"}
        issue_keywords -= stop_words
        
        common = intent_keywords.intersection(issue_keywords)
        
        # If > 50% match of the issue keywords
        if len(issue_keywords) > 0 and len(common) / len(issue_keywords) > 0.5:
             warnings.append(f"⚠️ History Warning: '{item['issue']}'\n   💡 Suggested Solution: {item['solution']}")
            
    return warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: prevention.py <command_or_intent>")
        sys.exit(1)
        
    input_str = sys.argv[1].strip()
    
    # Heuristic: Determine if it's a raw shell command or a natural language intent
    # Commands usually start with a known executable or contain shell pipes/redirects
    shell_verbs = ["python", "pip", "git", "npm", "node", "rm", "del", "copy", "move", "mkdir", "ffmpeg"]
    is_command = any(input_str.lower().startswith(v) for v in shell_verbs) or "|" in input_str or ">" in input_str
    
    warnings = []
    
    # 1. ALWAYS scan against History (Mistake Book)
    # This prevents repeating past mistakes even in natural language
    warnings.extend(scan_intent(input_str))
    
    # 2. If it's a command, scan for Hardcoded Red Lines
    if is_command:
        warnings.extend(scan_command(input_str))
        
    if warnings:
        print(f"\n{Colors.WARNING}🛡️ [The Shield] Pre-Flight Risk Detected:{Colors.ENDC}")
        for w in warnings:
            print(f"  {w}")
        sys.exit(1)
    else:
        print(f"{Colors.OKGREEN}✅ [The Shield] Safe to proceed.{Colors.ENDC}")
        sys.exit(0)

if __name__ == "__main__":
    main()
