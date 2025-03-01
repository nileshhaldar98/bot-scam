import os

# 📍 Set your GitHub repository path
REPO_PATH = "/Users/nileshhaldar98/Develpoer/bot-scam"

# Move into the repository
os.chdir(REPO_PATH)

print("🔍 Finding and deleting all 2019 commits...")

# 🛠️ Run git filter-repo to remove all 2019 commits
os.system('git filter-repo --commit-callback \''
          'commit_date = int(commit.original_committer_date)\n'
          'if 1546300800 <= commit_date < 1577836800:  # 2019 timestamp range\n'
          '    commit.skip()\''
)

print("✅ 2019 commits removed!")

# 🚀 Force push the cleaned history to GitHub
print("🔄 Pushing changes to GitHub...")
os.system("git push origin --force --all")

print("🎉 Done! 2019 commits should disappear within an hour.")