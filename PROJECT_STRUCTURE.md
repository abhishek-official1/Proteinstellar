# Proteinstellar Project Structure

This document describes the organization of the Proteinstellar repository.

## Directory Layout

```
proteinstellar/
├── .github/                          # GitHub-specific files
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md            # Bug report template
│       └── feature_request.md       # Feature request template
│
├── docs/                            # Documentation files
│   ├── getting_started.md          # Beginner's guide
│   └── examples.md                 # Detailed usage examples
│
├── notebooks/                       # Jupyter notebooks
│   ├── README.md                   # Notebooks documentation
│   ├── AlphaFold2.ipynb           # Structure prediction notebook
│   └── Proteinstellar_.ipynb      # Structure analysis notebook
│
├── plans/                          # Project planning documents
│
├── .gitignore                      # Git ignore rules
├── CHANGELOG.md                    # Version history
├── CITATION.bib                    # Academic citations (BibTeX)
├── CONTRIBUTING.md                 # Contribution guidelines
├── LICENSE                         # MIT License
├── PROJECT_ARCHITECTURE.md         # Technical architecture
├── PROJECT_STRUCTURE.md           # This file
├── README.md                       # Main documentation
├── requirements.txt                # Python dependencies
├── setup.py                        # Installation script
│
├── AlphaFold2.ipynb               # [Can be moved/removed after notebooks/ copy]
├── Proteinstellar_.ipynb          # [Can be moved/removed after notebooks/ copy]
├── movie6.mp4                      # Demo video
├── Protein Steller.docx.pdf       # Technical documentation PDF
└── Proteinstellar-...pdf           # Presentation slides PDF
```

## File Descriptions

### Root Directory

| File | Purpose |
|------|---------|
| `README.md` | Main project documentation, quick start guide |
| `LICENSE` | MIT License text |
| `requirements.txt` | Python package dependencies |
| `setup.py` | Python package installation script |
| `.gitignore` | Files/directories to exclude from Git |
| `CHANGELOG.md` | Version history and release notes |
| `CONTRIBUTING.md` | Guidelines for contributors |
| `CITATION.bib` | Academic citation information |
| `PROJECT_ARCHITECTURE.md` | Detailed technical documentation |
| `PROJECT_STRUCTURE.md` | Repository organization (this file) |

### .github/

GitHub-specific configuration and templates:
- `ISSUE_TEMPLATE/bug_report.md` - Standardized bug reporting
- `ISSUE_TEMPLATE/feature_request.md` - Feature request format

### docs/

Comprehensive documentation:
- `getting_started.md` - Installation, first prediction, troubleshooting
- `examples.md` - Detailed use cases and parameter configurations

### notebooks/

Executable Jupyter notebooks:
- `AlphaFold2.ipynb` - Main prediction pipeline
- `Proteinstellar_.ipynb` - Analysis and validation pipeline
- `README.md` - Notebook-specific documentation

### plans/

Project planning, roadmap, and internal documents (optional, can be kept private)

## Recommended Organization for Results

When running predictions, organize outputs as:

```
results/
├── projectname_001/
│   ├── jobname.result.zip
│   ├── jobname_unrelaxed_rank_001.pdb
│   ├── jobname_relaxed_rank_001.pdb
│   ├── jobname_pae.png
│   ├── jobname_plddt.png
│   └── jobname_coverage.png
│
└── projectname_002/
    └── ...
```

**Note:** The `results/` directory should be added to `.gitignore` to avoid committing large files.

## Development Structure (Optional)

For contributors developing additional features:

```
src/                                # Source code (future)
├── proteinstellar/
│   ├── __init__.py
│   ├── prediction/
│   │   ├── alphafold.py
│   │   └── msa.py
│   ├── analysis/
│   │   ├── dssp.py
│   │   └── blast.py
│   └── utils/
│       └── config.py
│
tests/                             # Test suite (future)
├── test_prediction.py
└── test_analysis.py
│
examples/                          # Example data (future)
├── sequences/
│   ├── p53.fasta
│   └── insulin.fasta
└── structures/
    └── 2ac0.pdb
```

## Usage Guidelines

### For End Users
1. Start with `README.md` for overview
2. Follow `docs/getting_started.md` for setup
3. Use `notebooks/AlphaFold2.ipynb` for predictions
4. Refer to `docs/examples.md` for advanced use cases

### For Contributors
1. Read `CONTRIBUTING.md` before starting
2. Check `PROJECT_ARCHITECTURE.md` for technical details
3. Follow coding standards
4. Update `CHANGELOG.md` with changes
5. Add tests for new features

### For Researchers
1. Cite using `CITATION.bib`
2. Report issues via GitHub Issues
3. Share improvements via Pull Requests

## File Maintenance

### Keep Updated
- `CHANGELOG.md` - Every release
- `requirements.txt` - When dependencies change
- `README.md` - Major feature additions
- Documentation - API or workflow changes

### Version Control
- Commit notebooks with cleared outputs
- Don't commit large data files (use `.gitignore`)
- Keep commit messages clear and descriptive

### Cleanup Recommendations
- Archive old result directories
- Remove duplicate PDF files if needed
- Consider moving demo video to external hosting for GitHub
- Consolidate duplicate notebook copies

## Additional Notes

**Large Files:**
- `movie6.mp4` (2.1 MB) - Consider Git LFS or external hosting
- PDF files (5+ MB) - Consider external documentation hosting
- Model parameters (not included) - Download via notebooks

**GitHub Repository Size:**
- Current: ~8 MB (without results)
- With large files: Consider Git LFS
- Recommended: <100 MB for free GitHub

**Future Enhancements:**
- Add `tests/` directory for unit tests
- Add `examples/` with sample data
- Add `scripts/` for automation
- Add `.dockerignore` and `Dockerfile` for containerization
- Add GitHub Actions workflows (`.github/workflows/`)

## Questions?

Refer to:
- [README.md](README.md) - General information
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [GitHub Issues](https://github.com/YOUR_USERNAME/proteinstellar/issues) - Support
