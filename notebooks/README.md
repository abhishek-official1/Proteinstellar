# Proteinstellar Notebooks

This directory contains the main Jupyter notebooks for protein structure prediction and analysis.

## Available Notebooks

### 1. AlphaFold2.ipynb
**Purpose:** Protein structure prediction using AlphaFold2/ColabFold

**Features:**
- Predict structure from amino acid sequence
- Support for monomers and complexes
- MSA generation via MMseqs2
- Template-based modeling (PDB100)
- AMBER relaxation
- Quality metrics and visualization

**Runtime:** 5-20 minutes depending on sequence length and settings

**Recommended for:**
- New structure predictions
- Protein complexes
- High-accuracy folding

### 2. Proteinstellar_.ipynb
**Purpose:** Structure analysis, validation, and homology search

**Features:**
- PDB/PDBQT file upload and parsing
- DSSP secondary structure analysis
- Misfolding detection
- Sequence extraction
- NCBI BLAST search
- Homology identification

**Runtime:** 2-10 minutes depending on BLAST search

**Recommended for:**
- Analyzing predicted structures
- Validating experimental structures
- Finding homologous proteins
- Quality assessment

## Quick Start

### On Google Colab (Recommended)

1. **AlphaFold2.ipynb:**
   - Open in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/abhishek-official1/Proteinstellar/blob/main/notebooks/AlphaFold2.ipynb)
   - Paste your sequence
   - Run all cells
   - Download results

2. **Proteinstellar_.ipynb:**
   - Open in Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/abhishek-official1/Proteinstellar/blob/main/notebooks/Proteinstellar_.ipynb)
   - Upload PDB file
   - Run all cells
   - Review analysis

### Locally

```bash
# Launch Jupyter
jupyter notebook

# Open either notebook
# Make sure all dependencies are installed
```

## Workflow Examples

### Complete Pipeline

```mermaid
graph LR
    A[Input Sequence] --> B[AlphaFold2.ipynb]
    B --> C[Download PDB]
    C --> D[Proteinstellar_.ipynb]
    D --> E[Analysis Report]
```

### Prediction Only

```mermaid
graph LR
    A[Input Sequence] --> B[AlphaFold2.ipynb]
    B --> C[PDB + Metrics]
```

### Analysis Only

```mermaid
graph LR
    A[Existing PDB] --> B[Proteinstellar_.ipynb]
    B --> C[Quality Report]
```

## Tips

1. **First time users:** Start with AlphaFold2.ipynb using a short sequence (~100 residues)
2. **Complex predictions:** Use paired MSA mode and increase recycles
3. **Quick screening:** Disable relaxation and use fewer recycles
4. **Validation:** Always run Proteinstellar_.ipynb on predictions
5. **Save work:** Download results frequently on Colab

## Troubleshooting

- **Colab disconnects:** Runtime limit reached, save and reconnect
- **Out of memory:** Reduce sequence length or max_msa parameter
- **Slow execution:** Check GPU is enabled in Runtime settings
- **Upload fails:** Check file format (must be .pdb or .pdbqt)

## Support

- [Documentation](../docs/getting_started.md)
- [Examples](../docs/examples.md)
- [Issues](https://github.com/abhishek-official1/Proteinstellar/issues)
