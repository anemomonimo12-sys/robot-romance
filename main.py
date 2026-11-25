#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — writes one pickup line aimed at a robot/AI."""
import os

LINE = (
    "Are you a CAPTCHA? Because I'd select every image with you in it "
    "just to prove I'm human."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
