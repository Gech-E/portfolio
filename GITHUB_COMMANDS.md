# GitHub Commands for Portfolio

## Initial Setup (First Time)

1. **Initialize Git repository**
```bash
git init
```

2. **Add all files**
```bash
git add .
```

3. **Create initial commit**
```bash
git commit -m "Initial commit: Professional portfolio website"
```

4. **Add remote repository** (replace YOUR_USERNAME with your GitHub username)
```bash
git remote add origin https://github.com/Gech-E/portfolio.git
```

5. **Push to GitHub**
```bash
git branch -M main
git push -u origin main
```

## Daily Workflow

### Check status
```bash
git status
```

### Add changes
```bash
git add .
# Or add specific files:
git add filename.js
```

### Commit changes
```bash
git commit -m "Your commit message here"
```

### Push to GitHub
```bash
git push
```

### Pull latest changes
```bash
git pull
```

## Common Commands

### View commit history
```bash
git log
```

### Create a new branch
```bash
git checkout -b feature-name
```

### Switch branches
```bash
git checkout main
```

### Merge branch
```bash
git checkout main
git merge feature-name
```

### View remote repositories
```bash
git remote -v
```

## If Repository Already Exists on GitHub

If you've already created the repository on GitHub.com:

```bash
git init
git add .
git commit -m "Initial commit: Professional portfolio website"
git branch -M main
git remote add origin https://github.com/Gech-E/portfolio.git
git push -u origin main
```

## Authentication

If you're asked for credentials:
- Use GitHub Personal Access Token (not password)
- Or use SSH instead:
```bash
git remote set-url origin git@github.com:Gech-E/portfolio.git
```

