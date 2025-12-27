# GitHub Setup Guide for Proteinstellar

This guide walks you through uploading your Proteinstellar project to GitHub.

## Prerequisites

- ✅ Git installed (version 2.51.2 detected)
- ✅ GitHub account created at https://github.com
- ✅ All project files prepared

## Step-by-Step Instructions

### 1. Initialize Git Repository

```bash
# Navigate to project directory
cd C:\Users\Admin\Downloads\protein

# Initialize Git
git init

# Check status
git status
```

### 2. Configure Git (First Time Only)

```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

### 3. Review .gitignore

The `.gitignore` file is already created and will exclude:
- Large video files (*.mp4)
- Notebook checkpoints
- Python cache files
- AlphaFold model parameters
- Result files and temporary data

### 4. Stage Files for Commit

```bash
# Add all files (respects .gitignore)
git add .

# Review what will be committed
git status
```

**Expected output:**
```
Changes to be committed:
  new file:   .gitignore
  new file:   README.md
  new file:   LICENSE
  new file:   requirements.txt
  new file:   CONTRIBUTING.md
  ... (and many more)
```

**Note:** `movie6.mp4` should NOT appear (excluded by .gitignore)

### 5. Create Initial Commit

```bash
git commit -m "Initial commit: Proteinstellar v1.0.0 - AlphaFold-based computational therapeutics platform"
```

### 6. Create GitHub Repository

**Option A: Via GitHub Website (Recommended)**

1. Go to https://github.com/new
2. Fill in the details:
   - **Repository name:** `proteinstellar` (or your preferred name)
   - **Description:** "Computational therapeutics platform for protein structure prediction and analysis using AlphaFold2"
   - **Visibility:** Public (recommended for open source) or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

**Option B: Via GitHub CLI (if gh is installed)**

```bash
gh repo create proteinstellar --public --description "Computational therapeutics platform using AlphaFold2"
```

### 7. Connect Local to GitHub

GitHub will show commands after creating the repo. Use these:

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/proteinstellar.git

# Verify remote
git remote -v

# Rename branch to main (if needed)
git branch -M main
```

### 8. Push to GitHub

```bash
# Push all commits
git push -u origin main
```

**If you're asked for credentials:**
- Use a Personal Access Token (PAT) instead of password
- Create PAT at: https://github.com/settings/tokens

### 9. Verify Upload

1. Go to https://github.com/YOUR_USERNAME/proteinstellar
2. You should see:
   - Professional README with badges
   - All documentation files
   - Notebooks in notebooks/ folder
   - LICENSE file
   - Clean repository structure

### 10. Configure Repository Settings

**Add Topics:**
1. Go to repository page
2. Click "⚙️ Settings" or the gear icon near "About"
3. Add topics:
   - `alphafold`
   - `protein-folding`
   - `bioinformatics`
   - `computational-biology`
   - `structural-biology`
   - `drug-discovery`
   - `jupyter-notebook`
   - `cancer-research`

**Update Description:**
- Add website (if any)
- Check "Releases" and "Packages"

**Enable Discussions (Optional):**
1. Settings → Features → Enable Discussions
2. Great for Q&A and community

**Add Repository Image:**
1. Upload a project logo (if you have one)
2. Dimensions: 1280x640 pixels recommended

### 11. Add Colab Badges to Notebooks

Update `notebooks/README.md` with your actual GitHub username:

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/proteinstellar/blob/main/notebooks/AlphaFold2.ipynb)
```

Then commit and push:

```bash
git add notebooks/README.md
git commit -m "docs: add Colab badges with correct repository URL"
git push
```

### 12. Update Placeholder URLs

Search and replace `YOUR_USERNAME` in these files:
- `README.md`
- `setup.py`
- `CONTRIBUTING.md`
- `docs/getting_started.md`
- `docs/examples.md`
- `notebooks/README.md`

```bash
# After updating files
git add .
git commit -m "docs: update repository URLs with actual username"
git push
```

## Post-Upload Checklist

- [ ] Repository is public/private as intended
- [ ] README displays correctly with badges
- [ ] LICENSE file is visible
- [ ] Notebooks can be opened in Colab
- [ ] All documentation links work
- [ ] Topics/tags are added
- [ ] Description is set
- [ ] .gitignore is working (large files excluded)

## Handling Large Files

### If movie6.mp4 was accidentally committed:

```bash
# Remove from Git history (use carefully!)
git rm --cached movie6.mp4
git commit -m "Remove large video file from repository"
git push
```

### For future large files, use Git LFS:

```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.mp4"
git lfs track "*.zip"

# Add .gitattributes
git add .gitattributes
git commit -m "Add Git LFS tracking"
git push
```

## Creating Your First Release

```bash
# Create a tag
git tag -a v1.0.0 -m "Release version 1.0.0 - Initial public release"

# Push tag to GitHub
git push origin v1.0.0
```

Then on GitHub:
1. Go to "Releases"
2. Click "Draft a new release"
3. Select tag v1.0.0
4. Title: "Proteinstellar v1.0.0"
5. Description: Copy from CHANGELOG.md
6. Attach any release assets (optional)
7. Click "Publish release"

## Common Issues and Solutions

### Issue: "Permission denied"
**Solution:** Set up SSH keys or use Personal Access Token
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to GitHub: Settings → SSH Keys → New SSH key
# Copy public key:
cat ~/.ssh/id_ed25519.pub

# Update remote URL to use SSH
git remote set-url origin git@github.com:YOUR_USERNAME/proteinstellar.git
```

### Issue: "Repository too large"
**Solution:** Check for accidentally committed large files
```bash
# Find large files
git ls-files | xargs -n 1 git ls-tree -r HEAD -- | sort -k 3 -nr | head -10

# Remove from history if needed
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH/TO/LARGE/FILE" \
  --prune-empty --tag-name-filter cat -- --all
```

### Issue: "Merge conflict"
**Solution:** Pull before pushing
```bash
git pull origin main --rebase
git push
```

## Maintaining Your Repository

### Regular Updates

```bash
# Make changes to files
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add new analysis feature"

# Push to GitHub
git push
```

### Creating Branches for Features

```bash
# Create and switch to new branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push branch
git push -u origin feature/new-feature

# Create Pull Request on GitHub
```

## Making Your Project Discoverable

1. **Star your own repo** (shows it's active)
2. **Share on social media** with relevant hashtags
3. **Add to awesome lists** (e.g., awesome-structural-biology)
4. **Post on forums:** r/bioinformatics, Research Gate
5. **Add to your publications** as supplementary material
6. **Create demo videos** and link in README
7. **Write blog posts** about the project
8. **Present at conferences**

## Analytics and Insights

GitHub provides analytics:
- **Traffic:** Views, unique visitors, clones
- **Community:** Contributors, forks, stars
- **Dependency graph:** Package dependencies
- **Security:** Vulnerability alerts

Access via: Repository → Insights

## Next Steps

1. **Create example predictions** in `examples/` directory
2. **Add unit tests** in `tests/` directory
3. **Set up GitHub Actions** for automated testing
4. **Create a project website** using GitHub Pages
5. **Write blog posts** or tutorials
6. **Engage with community** via Issues and Discussions

## Resources

- [GitHub Docs](https://docs.github.com)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Git LFS](https://git-lfs.github.com/)

## Need Help?

- [GitHub Community Forum](https://github.community/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/github)
- [Git Documentation](https://git-scm.com/doc)

---

**Congratulations!** 🎉 Your Proteinstellar project is now on GitHub!
