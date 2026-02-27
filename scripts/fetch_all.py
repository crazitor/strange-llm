#!/usr/bin/env python3
"""Master script to run all research fetchers in sequence."""
import subprocess
import sys
import os
import time

PYTHON = "/usr/local/opt/python@3.11/bin/python3.11"
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

FETCHERS = [
    ("LessWrong + Alignment Forum", "fetch_lw_af.py"),
    ("Substack Blogs", "fetch_substacks.py"),
    ("Stanford Encyclopedia", "fetch_sep.py"),
    ("Internet Encyclopedia of Philosophy", "fetch_iep.py"),
    ("Chalmers Papers", "fetch_chalmers.py"),
    ("Floridi Papers", "fetch_floridi.py"),
    ("Multi-Philosopher Papers", "fetch_philosophers.py"),
    ("PhilPapers", "fetch_philpapers.py"),
    ("ArXiv Papers", "fetch_arxiv.py"),
    ("Alignment Forum (Dedicated)", "fetch_af.py"),
    ("Scott Aaronson Blog", "fetch_aaronson.py"),
]

def main():
    print("=" * 60)
    print("  AI Philosophy Research Fetcher")
    print("=" * 60)

    results = {}
    for name, script in FETCHERS:
        print(f"\n{'='*60}")
        print(f"  Starting: {name}")
        print(f"{'='*60}")
        start = time.time()
        script_path = os.path.join(SCRIPTS_DIR, script)
        try:
            result = subprocess.run(
                [PYTHON, script_path],
                cwd=os.path.join(SCRIPTS_DIR, ".."),
                capture_output=False,
                timeout=1800,  # 30 min max per fetcher
            )
            elapsed = time.time() - start
            results[name] = "OK" if result.returncode == 0 else f"FAIL (exit {result.returncode})"
            print(f"\n  {name}: completed in {elapsed:.1f}s")
        except subprocess.TimeoutExpired:
            results[name] = "TIMEOUT"
            print(f"\n  {name}: TIMEOUT")
        except Exception as e:
            results[name] = f"ERROR: {e}"
            print(f"\n  {name}: ERROR: {e}")

    # Summary
    print(f"\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    for name, status in results.items():
        print(f"  {name}: {status}")

    # Count files
    research_dir = os.path.join(SCRIPTS_DIR, "..", "research")
    total_files = 0
    total_size = 0
    for root, dirs, files in os.walk(research_dir):
        for f in files:
            fp = os.path.join(root, f)
            total_files += 1
            total_size += os.path.getsize(fp)
    print(f"\n  Total files: {total_files}")
    print(f"  Total size: {total_size / 1024 / 1024:.1f} MB")

if __name__ == "__main__":
    main()
