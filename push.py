import os
import sys

os.system("git init")
os.system("git remote add origin https://github.com/rshnGhost/django-space.git")
os.system("git config --local user.name 'rshnGhost'")
os.system("git config --local user.email '31742263+rshnGhost@users.noreply.github.com'")
os.system("git branch -m main")
os.system("git status")
os.system("git add .")
os.system("git status")
os.system(f'git commit -m "{str("".join(sys.argv[1:]))}"')
os.system("git switch main")
os.system("git push origin main")
