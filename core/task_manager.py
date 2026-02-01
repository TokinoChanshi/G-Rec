import sys
import argparse
import re
from pathlib import Path
from datetime import datetime

try:

    from .config import CORE_DIR, force_utf8, Colors

except (ImportError, ValueError):

    sys.path.append(str(Path(__file__).parent))

    from config import CORE_DIR, force_utf8, Colors



# Initialize

force_utf8()

QUEUE_FILE = CORE_DIR / "TASK_QUEUE.md"



# Templates

HEADER = f"# 📋 G-Rec 任务队列 (Task Queue)\n"

SECTIONS = ["📥 收件箱 (Inbox)", "🚀 进行中 (Active)", "📅 待办 (Backlog)", "✅ 已完成 (Completed)", "🗑️ 归档 (Archived)"]



def init_queue():

    """Initialize the queue file with standard sections if it looks broken or empty."""

    if not QUEUE_FILE.exists() or QUEUE_FILE.stat().st_size < 10:

        content = HEADER + "\n"

        for sec in SECTIONS:

            content += f"## {sec}\n\n"

        with open(QUEUE_FILE, "w", encoding="utf-8") as f:

            f.write(content)

        print(f"{Colors.OKGREEN}✅ Initialized new TASK_QUEUE.md{Colors.ENDC}")



def read_tasks():

    if not QUEUE_FILE.exists():

        init_queue()

    with open(QUEUE_FILE, "r", encoding="utf-8") as f:

        return f.readlines()



def write_tasks(lines):

    with open(QUEUE_FILE, "w", encoding="utf-8") as f:

        f.writelines(lines)



def add_task(description, section="Inbox"):

    """Adds a task to the top of the specified section."""

    lines = read_tasks()

    new_lines = []

    target_section_found = False

    inserted = False

    

    # Normalize section name (case insensitive matching)

    # Map 'inbox' -> '📥 收件箱 (Inbox)'

    target_header = None

    for s in SECTIONS:

        # Check if 'inbox' is in '📥 收件箱 (Inbox)'

        if section.lower() in s.lower():

            target_header = s

            break

            

    if not target_header:

        target_header = SECTIONS[0] # Default to Inbox



    # Determine status based on section

    is_completed_section = "Completed" in target_header or "Archived" in target_header or "已完成" in target_header or "归档" in target_header

    checkbox = "[x]" if is_completed_section else "[ ]"

    

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    new_task_line = f"- {checkbox} **{description}** (Added: {timestamp})\n"



    for line in lines:

        new_lines.append(line)

        if line.strip().startswith("##") and target_header in line:

            target_section_found = True

            new_lines.append(new_task_line)

            inserted = True

    

    if not target_section_found:

        # Section missing, append it

        new_lines.append(f"\n## {target_header}\n")

        new_lines.append(new_task_line)

        inserted = True



    write_tasks(new_lines)

    print(f"{Colors.OKGREEN}✅ Added task to [{target_header}]: {description}{Colors.ENDC}")



def list_tasks(status="all"):

    """List tasks, optionally filtering by status (open/done)."""

    lines = read_tasks()

    current_section = "Unknown"

    print(f"\n{Colors.OKCYAN}📋 Task Queue ({status}):{Colors.ENDC}")

    

    for line in lines:

        line = line.strip()

        if line.startswith("## "):

            current_section = line.replace("## ", "")

            print(f"\n{Colors.BOLD}{current_section}{Colors.ENDC}")

        elif line.startswith("- ["):

            is_done = line.startswith("- [x]")

            if status == "open" and is_done: continue

            if status == "done" and not is_done: continue

            print(f"  {line}")



def complete_task(keyword):

    """Mark a task as complete by keyword match."""

    lines = read_tasks()

    new_lines = []

    modified_count = 0

    

    for line in lines:

        if line.strip().startswith("- [ ]") and keyword.lower() in line.lower():

            # Mark as done

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

            new_line = line.replace("- [ ]", "- [x]").strip()

            # Optional: Move to Completed section? For now, just mark [x].

            # Append completion time if not present

            if "(Completed:" not in new_line:

                new_line += f" (Done: {timestamp})"

            new_lines.append(new_line + "\n")

            print(f"{Colors.OKGREEN}✅ Completed: {line.strip()[6:]}{Colors.ENDC}")

            modified_count += 1

        else:

            new_lines.append(line)

            

    if modified_count > 0:

        write_tasks(new_lines)

    else:

        print(f"{Colors.WARNING}⚠️ No open task found matching '{keyword}'{Colors.ENDC}")



def archive_completed():

    """Moves all [x] tasks to the Archive section."""

    lines = read_tasks()

    active_lines = []

    archive_lines = []

    

    archive_header_exists = False

    

    current_section = ""

    

    for line in lines:

        if line.startswith("## "):

            current_section = line.strip()

            if "Archived" in current_section:

                archive_header_exists = True

            active_lines.append(line)

            continue

            

        if line.strip().startswith("- [x]"):

            # It's a completed task

            if "Archived" in current_section:

                # Already in archive, keep it there

                active_lines.append(line)

            else:

                # Move to pending archive list

                archive_lines.append(line)

        else:

            active_lines.append(line)



    if not archive_lines:

        print(f"{Colors.OKBLUE}ℹ️ No completed tasks to archive.{Colors.ENDC}")

        return



    # Now append archive lines to the "Archived" section in active_lines

    final_lines = []

    archive_section_processed = False

    

    for line in active_lines:

        final_lines.append(line)

        if "## 🗑️ 归档 (Archived)" in line:

            final_lines.extend(archive_lines)

            archive_section_processed = True

            

    if not archive_section_processed:

        # If header wasn't found in loop (shouldn't happen if init is correct, but safe fallback)

        final_lines.append("\n## 🗑️ 归档 (Archived)\n")

        final_lines.extend(archive_lines)



    write_tasks(final_lines)

    print(f"{Colors.OKBLUE}📦 Archived {len(archive_lines)} tasks.{Colors.ENDC}")

def main():
    parser = argparse.ArgumentParser(description="G-Rec Task Manager")
    subparsers = parser.add_subparsers(dest="command")
    
    # Add
    add_p = subparsers.add_parser("add")
    add_p.add_argument("description", help="Task description")
    add_p.add_argument("--section", default="Inbox", help="Target section (Inbox, Active, Backlog)")
    
    # List
    list_p = subparsers.add_parser("list")
    list_p.add_argument("--status", choices=["all", "open", "done"], default="all")
    
    # Done
    done_p = subparsers.add_parser("done")
    done_p.add_argument("keyword", help="Keyword to identify the task")
    
    # Archive
    subparsers.add_parser("archive")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.description, args.section)
    elif args.command == "list":
        list_tasks(args.status)
    elif args.command == "done":
        complete_task(args.keyword)
    elif args.command == "archive":
        archive_completed()
    else:
        # Default behavior: list open
        list_tasks("open")

if __name__ == "__main__":
    main()
