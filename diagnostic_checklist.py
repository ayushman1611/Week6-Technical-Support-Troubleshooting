#!/usr/bin/env python3
"""Week 6 support checklist utility.
Training/demo use only. No real credentials or production changes.
"""

CHECKLIST = [
    "Record incident ID, reporter, time, service, and symptoms",
    "Determine scope and business impact",
    "Assign P1/P2/P3/P4 severity",
    "Check monitoring and recent changes",
    "Collect logs, timestamps, screenshots, and request IDs",
    "Reproduce safely with test data",
    "Identify likely fault domain",
    "Apply approved workaround or fix",
    "Verify the original failure is resolved",
    "Communicate status and resolution",
    "Document root cause",
    "Record preventive action and escalation"
]

def run_checklist():
    print("\nWEEK 6 TECHNICAL SUPPORT CHECKLIST\n")
    for i, item in enumerate(CHECKLIST, 1):
        print(f"{i:02d}. [ ] {item}")

if __name__ == "__main__":
    run_checklist()
