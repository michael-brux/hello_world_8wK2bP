#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

def run_build_script():
    # --- 1. Determine the Project Root ---
    # Current script is in: <project_root>/scripts/
    # We resolve: script_file -> scripts_dir -> project_root
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent

    print(f"Executing build from: {project_root}")

    # --- 2. Define Commands ---
    # We use sys.executable to ensure we use the SAME python interpreter 
    # that is running this script (e.g., inside your venv)
    
    commands = [
        # Command 1: python3 -m pip install --upgrade build
        [sys.executable, "-m", "pip", "install", "--upgrade", "build"],
        
        # Command 2: python3 -m build
        [sys.executable, "-m", "build"]
    ]

    # --- 3. Execute Commands Sequentially ---
    try:
        for cmd in commands:
            print(f"Running: {' '.join(cmd)}")
            # cwd=project_root ensures the build happens at the top level of the project
            subprocess.run(cmd, cwd=project_root, check=True)
            
        print("\nBuild completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"\nError: Command failed with return code {e.returncode}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    run_build_script()
