import os
from datetime import datetime, timedelta
import subprocess

# 📍 Set your GitHub repository path
REPO_PATH = "/Users/nileshhaldar98/Develpoer/bot-scam"

# Move into the repository
os.chdir(REPO_PATH)

print("🔍 Creating commits for the last 10 days...")

# Ensure git is initialized
if not os.path.exists('.git'):
    subprocess.run(['git', 'init'])

# Get current date
current_date = datetime.now()

# Create commits for last 10 days
for i in range(10):
    # Calculate the date for this commit
    commit_date = current_date - timedelta(days=i)
    date_string = commit_date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Create a unique commit with the specific date
    with open('timestamp.txt', 'w') as f:
        f.write(f'Update for {date_string}\nRandom: {os.urandom(8).hex()}')
    
    # Use subprocess for better command execution
    subprocess.run(['git', 'add', 'timestamp.txt'])
    subprocess.run(['git', 'commit', '--date', date_string, '-m', f'Update for {date_string}'], 
                  env=dict(os.environ, GIT_AUTHOR_DATE=date_string, GIT_COMMITTER_DATE=date_string))

print("✅ Commits created for the last 10 days!")

# 🚀 Push changes to GitHub
print("🔄 Pushing changes to GitHub...")

# Ensure we have a main branch
subprocess.run(['git', 'branch', '-M', 'main'])

# Check if remote exists
remote_exists = subprocess.run(['git', 'remote', 'get-url', 'origin'], capture_output=True, text=True).returncode == 0

if not remote_exists:
    # Prompt for GitHub repository URL
    repo_url = input("Enter your GitHub repository URL (e.g., https://github.com/username/repo.git): ")
    subprocess.run(['git', 'remote', 'add', 'origin', repo_url])

try:
    # Try to push changes
    result = subprocess.run(['git', 'push', '-u', 'origin', 'main', '--force'], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("🎉 Success! Green boxes should appear on your GitHub profile soon.")
    else:
        print("❌ Push failed. Error:", result.stderr)
        print("""
Make sure you have:
1. Correct repository URL
2. Proper GitHub authentication (SSH key or credential helper)
3. Required permissions for the repository""")
except Exception as e:
    print(f"❌ An error occurred: {str(e)}")