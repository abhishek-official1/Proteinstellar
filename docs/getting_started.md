# Getting Started with Proteinstellar

## Table of Contents
1. [Quick Start Guide](#quick-start-guide)
2. [First Prediction](#your-first-prediction)
3. [Understanding Results](#understanding-results)
4. [Common Use Cases](#common-use-cases)
5. [Troubleshooting](#troubleshooting)

## Quick Start Guide

### Option 1: Google Colab (Recommended for Beginners)

**Advantages:**
- No installation required
- Free GPU access
- Pre-configured environment

**Steps:**
1. Open [AlphaFold2.ipynb](../AlphaFold2.ipynb) in Google Colab
2. Sign in with your Google account
3. Click `Runtime` → `Change runtime type` → Select "GPU"
4. You're ready to go!

### Option 2: Local Installation

**Requirements:**
- Python 3.8 or higher
- 8GB+ RAM (16GB recommended)
- GPU with CUDA support (optional but recommended)

**Installation:**
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/proteinstellar.git
cd proteinstellar

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install DSSP (for structure analysis)
# Ubuntu/Debian:
sudo apt-get install dssp
# macOS:
brew install dssp

# Launch Jupyter
jupyter notebook
```

## Your First Prediction

### Example 1: Predict a Protein Structure

Let's predict the structure of a small protein (Ubiquitin):

```python
# In AlphaFold2.ipynb
query_sequence = '''
MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG
'''

jobname = 'ubiquitin_test'
```

**What happens:**
1. MSA generation (~2-5 minutes)
2. AlphaFold2 prediction (~5-10 minutes)
3. AMBER relaxation (if enabled, ~2-5 minutes)
4. Result visualization

### Example 2: Predict a Protein Complex

For a homodimer, use `:` to separate chains:

```python
query_sequence = 'SEQUENCE1:SEQUENCE1'  # Homodimer
# or
query_sequence = 'SEQUENCE1:SEQUENCE2'  # Heterodimer
```

### Example 3: Analyze an Existing Structure

1. Open [Proteinstellar_.ipynb](../Proteinstellar_.ipynb)
2. Upload your PDB file when prompted
3. Run all cells
4. Review:
   - Misfolding detection results
   - BLAST homology search
   - Sequence extraction

## Understanding Results

### Structure Quality Metrics

**pLDDT (predicted Local Distance Difference Test)**
- Range: 0-100
- >90: Very high confidence (backbone well-predicted)
- 70-90: Good confidence (generally correct)
- 50-70: Low confidence (questionable)
- <50: Very low confidence (likely disordered)

**PAE (Predicted Aligned Error)**
- Lower is better
- Shows confidence in relative positions
- Important for protein complexes

**pTMscore (predicted Template Modeling score)**
- Range: 0-1
- >0.8: High confidence in overall fold
- 0.5-0.8: Medium confidence
- <0.5: Low confidence

### Output Files

```
jobname/
├── jobname_unrelaxed_rank_001.pdb    # Best predicted structure
├── jobname_relaxed_rank_001.pdb      # After AMBER relaxation
├── jobname_scores_rank_001.json      # Quality metrics
├── jobname_pae.png                   # PAE heatmap
├── jobname_plddt.png                 # pLDDT plot
├── jobname_coverage.png              # MSA coverage
└── jobname.result.zip                # All results packaged
```

## Common Use Cases

### Use Case 1: Cancer Research (p53 Analysis)

```python
# P53 DNA-binding domain sequence
query_sequence = '''
SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENL
'''

jobname = 'p53_DBD'
template_mode = "pdb100"  # Use templates for better accuracy
```

### Use Case 2: Antibody Design

```python
# Heavy chain : Light chain
query_sequence = 'HEAVY_CHAIN_SEQ:LIGHT_CHAIN_SEQ'
pair_mode = "paired"
num_recycles = "6"  # More recycles for better accuracy
```

### Use Case 3: Protein Engineering Validation

After designing a mutation, predict the structure:

```python
# Wild-type and mutant
query_sequence_wt = 'ORIGINAL_SEQUENCE'
query_sequence_mut = 'MUTATED_SEQUENCE'

# Compare pLDDT and PAE values
```

## Troubleshooting

### Common Issues

**Issue: "Runtime disconnected"**
- Colab free tier has time limits
- Save work frequently
- Reconnect and continue

**Issue: "Out of memory"**
- Sequence too long for GPU
- Reduce `max_msa` parameter
- Split long sequences

**Issue: "MSA generation failed"**
- Check internet connection
- MMseqs2 server may be busy
- Try again later

**Issue: "Low pLDDT scores"**
- Protein may be intrinsically disordered
- Try using templates (`template_mode = "pdb100"`)
- Check if sequence is correct

**Issue: "BLAST search timeout"**
- NCBI server may be slow
- Use shorter sequences
- Run standalone BLAST locally

### Performance Tips

1. **Faster predictions:**
   - Use `num_relax = 0` (skip AMBER)
   - Reduce `num_recycles` to 1
   - Use `max_msa = "64:128"`

2. **Better accuracy:**
   - Use `template_mode = "pdb100"`
   - Increase `num_recycles` to 6
   - Enable `use_dropout = True` with `num_seeds = 5`

3. **Complex predictions:**
   - Use `model_type = "alphafold2_multimer_v3"`
   - Set `pair_mode = "paired"`
   - Use more recycles

## Next Steps

- Read [PROJECT_ARCHITECTURE.md](../PROJECT_ARCHITECTURE.md) for technical details
- Check [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute
- Join discussions on GitHub
- Explore advanced parameters

## Need Help?

- [GitHub Issues](https://github.com/YOUR_USERNAME/proteinstellar/issues)
- [Discussions](https://github.com/YOUR_USERNAME/proteinstellar/discussions)
- [AlphaFold FAQ](https://alphafold.ebi.ac.uk/faq)
- [ColabFold GitHub](https://github.com/sokrypton/ColabFold)
