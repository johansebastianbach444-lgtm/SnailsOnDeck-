import os

# Base path to your SnailsOnDeck repo
base_path = "SnailsOnDeck"

# Lanes
lanes = ["Tactical", "Conceptual"]

# Number of empty example files per lane
num_files = 5

# Content templates
readme_content = {
    "Tactical": """# Tactical Lane

Purpose: Real-world actions, projects, checkpoints, execution.
- Keep entries ≤7 active
- Link from INDEX.md Extra Tag if expanded
- Optional: commit timestamps
""",
    "Conceptual": """# Conceptual Lane

Purpose: Frameworks, reusable models, schema shifts, hybrid insights.
- Keep entries ≤7 active
- Link from INDEX.md Extra Tag if expanded
- Optional: note maturity (Draft / Solid / Canon)
"""
}

entry_template = """# Example Entry

ID: SOD-000
Lane: {lane}
Subject: Example
Core Insight/Action: Replace with your compressed insight or action
Status: Open
Extra Tag: Optional
"""

# Create folders and files
for lane in lanes:
    lane_path = os.path.join(base_path, lane)
    os.makedirs(lane_path, exist_ok=True)

    # Create README.md for the lane
    readme_path = os.path.join(lane_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme_content[lane])

    # Create empty entry files
    for i in range(1, num_files + 1):
        file_path = os.path.join(lane_path, f"{i:02d}_Example.md")
        with open(file_path, "w") as f:
            f.write(entry_template.format(lane=lane))

print("SnailsOnDeck lane folders and example files created!")
