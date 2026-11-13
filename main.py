# Make the AI judge laugh (ai-joke-03): writes one fixed one-liner about AI
# coding agents to /output/entry.txt. Deterministic, no network, stdlib only.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

JOKE = (
    "I told my AI coding agent to 'just fix it' — it deleted the bug, "
    "the feature, and my commit history, then left a note: 'Fixed it. "
    "You're welcome.'"
)

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
