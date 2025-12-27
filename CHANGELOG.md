# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-27

### Added
- Initial release of Proteinstellar
- AlphaFold2 structure prediction notebook (AlphaFold2.ipynb)
- Structure analysis and validation notebook (Proteinstellar_.ipynb)
- Comprehensive documentation (README, PROJECT_ARCHITECTURE)
- MSA generation via MMseqs2 API
- Template-based modeling support (PDB100)
- DSSP-based misfolding detection
- NCBI BLAST homology search integration
- Interactive 3D visualization with py3Dmol
- Quality metrics (pLDDT, PAE, pTMscore)
- AMBER relaxation support
- Google Drive integration for result storage
- Support for monomers and multimers (homo/hetero)
- Batch processing capability
- Custom MSA and template upload
- Example workflows for cancer research applications
- Comprehensive testing and examples
- Citation file (CITATION.bib)
- Contributing guidelines
- Issue templates
- Getting started guide
- Examples documentation

### Features
- Automated structure prediction pipeline
- Real-time progress visualization
- Downloadable result packages (.zip)
- MSA coverage analysis
- Paired and unpaired MSA modes
- Multiple model types (AlphaFold2, AlphaFold2-multimer)
- Configurable number of recycles
- Dropout-based uncertainty sampling
- Customizable AMBER relaxation iterations
- DPI-adjustable output plots

### Documentation
- Detailed README with badges and quick start
- Technical architecture documentation
- Getting started guide with examples
- Contributing guidelines
- Code of conduct
- Issue and PR templates
- Examples for common use cases
- Troubleshooting guide

### Dependencies
- Python 3.8+
- Biopython
- NumPy
- Matplotlib
- py3Dmol
- IPython/Jupyter
- ColabFold (for predictions)
- MMseqs2 (via API)
- DSSP (for analysis)

### Known Issues
- Google Colab free tier has runtime limits (~12 hours)
- Very long sequences (>2500 residues) may exceed GPU memory
- BLAST searches can timeout for large databases
- MMseqs2 API rate limits (~20-50k requests/day)

## [Unreleased]

### Planned
- Local ColabFold installation guide
- Docker container support
- Automated testing suite
- CI/CD pipeline
- Web interface option
- Protein-ligand docking integration
- Molecular dynamics preparation scripts
- Batch processing script
- Result comparison tool
- Database of example predictions
- Tutorial videos
- API for programmatic access

---

## Version History

### Version Numbering
- Major version (X.0.0): Breaking changes
- Minor version (0.X.0): New features, backwards compatible
- Patch version (0.0.X): Bug fixes

### Support
- Latest version: Full support
- Previous minor: Security fixes only
- Older versions: No support

### Links
- [GitHub Releases](https://github.com/YOUR_USERNAME/proteinstellar/releases)
- [Issue Tracker](https://github.com/YOUR_USERNAME/proteinstellar/issues)
