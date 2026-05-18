#!/usr/bin/env python3
"""
Quick capture script for SecondBrain vault.
Appends timestamped notes to the Inbox.
"""

import sys
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent
INBOX_PATH = VAULT_ROOT / "Knowledge" / "Inbox.md"


def capture_note(note: str):
    """Append a timestamped note to the inbox."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    inbox_content = f"\n\n## {timestamp}\n{note}\n"
    
    with open(INBOX_PATH, "a") as f:
        f.write(inbox_content)
    
    print(f"Note captured to Inbox.md at {timestamp}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python inbox_capture.py 'your note here'")
        sys.exit(1)
    
    note = " ".join(sys.argv[1:])
    capture_note(note)
