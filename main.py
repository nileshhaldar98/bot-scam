import os
import subprocess
import random

# 📍 Set your GitHub repository path
REPO_PATH = "/Users/nileshhaldar98/Develpoer/bot-scam"

# 🎯 Move into the GitHub repo folder
os.chdir(REPO_PATH)

# 📂 Define language files and sizes (in KB)
files = {
    "main.js": 760,   # 76% JavaScript
    "app.java": 80,   # 8% Java
    "script.py": 60,  # 6% Python
    "program.c": 50,  # 5% C
    "code.cpp": 50    # 5% C++
}

# 📄 Function to create files with specified sizes
def create_files():
    for filename, size_kb in files.items():
        with open(filename, "w") as file:
            file.write(f"// {filename}\n")
            file.write("A" * (size_kb * 1024))  # Fill with junk data

# 🚀 Function to commit and push changes
def commit_changes():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Added files to manipulate language stats"])
    subprocess.run(["git", "push"])

# 🔥 Run everything automatically
create_files()
commit_changes()