"""
ach-return-codes / ach.py
Author:  Raghav Anand
Created: 2026-11-06

Look up ACH return codes from the command line.

How to run:
  python3 ach.py          # interactive: type a code like R01, 'list' or 'quit'
  python3 ach.py R01      # one-shot lookup
"""

import sys

from codes import CODES


def normalize(code):
    """Turn user input like ' r1 ' or 'R01' into the standard form 'R01'."""
    code = code.strip().upper()
    if code.startswith("R") and code[1:].isdigit():
        return f"R{int(code[1:]):02d}"
    return code


def lookup(code):
    """Return the facts for a code, or None if we don't know it."""
    return CODES.get(normalize(code))


def format_card(code):
    """Build the text block shown to the user for one code."""
    info = lookup(code)
    if info is None:
        return f"Unknown code: {code.strip()}. Type 'list' to see supported codes."
    return "\n".join([
        f"{normalize(code)}: {info['title']}",
        f"  What it means:  {info['meaning']}",
        f"  Can you retry?  {info['retry']}",
        f"  Return window:  {info['window']}",
        f"  Tell customer:  \"{info['customer_message']}\"",
    ])


def list_codes():
    """One line per supported code."""
    return "\n".join(f"  {code}  {info['title']}" for code, info in CODES.items())


def main():
    # One-shot mode: python3 ach.py R01
    if len(sys.argv) > 1:
        print(format_card(sys.argv[1]))
        return

    # Interactive mode
    print("ACH Return Code Explainer. Type a code (e.g. R01), 'list', or 'quit'.")
    while True:
        entry = input("\ncode> ").strip()
        if entry.lower() in ("quit", "exit", "q"):
            break
        if entry.lower() == "list":
            print(list_codes())
        elif entry:
            print(format_card(entry))


if __name__ == "__main__":
    main()