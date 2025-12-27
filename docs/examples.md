# Proteinstellar Examples

This document provides detailed examples for common use cases.

## Table of Contents
1. [Basic Structure Prediction](#basic-structure-prediction)
2. [Protein Complex Prediction](#protein-complex-prediction)
3. [Structure Analysis Pipeline](#structure-analysis-pipeline)
4. [Cancer Research Applications](#cancer-research-applications)
5. [Advanced Configurations](#advanced-configurations)

## Basic Structure Prediction

### Example 1: Small Protein (Insulin)

**Sequence:** Human Insulin Chain A (21 residues)

```python
query_sequence = 'GIVEQCCTSICSLYQLENYCN'
jobname = 'insulin_chain_a'
num_relax = 1
template_mode = "none"
```

**Expected Runtime:** 3-5 minutes
**Expected pLDDT:** >85 (high confidence)

### Example 2: Medium Protein (p53 DNA-Binding Domain)

**Sequence:** p53 DBD (residues 94-312, 219 amino acids)

```python
query_sequence = '''
SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENL
'''
jobname = 'p53_DBD'
num_relax = 5
template_mode = "pdb100"
num_recycles = 6
```

**Expected Runtime:** 10-15 minutes
**Known structure:** PDB ID 2AC0 (for validation)

## Protein Complex Prediction

### Example 3: Homodimer

**Case:** p53 tetramerization domain dimer

```python
# Same sequence twice, separated by ':'
query_sequence = '''
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD:GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
'''
jobname = 'p53_TD_dimer'
model_type = "alphafold2_multimer_v3"
pair_mode = "paired"
num_recycles = 12
```

**Expected PAE:** <5 Å at interface (high confidence)

### Example 4: Heterodimer (Antibody Fv Fragment)

```python
# Heavy chain : Light chain
query_sequence = '''
EVQLVESGGGLVQPGGSLRLSCAASGFTFSSYGMHWVRQAPGKGLEWVAVIWYDGSNKYYADSVKGRFTISRDNSKNTLYLQMNSLRAEDTAVYYCARDGYYGDYELFDYWGQGTLVTVSS:DIQMTQSPSSLSASVGDRVTITCRASQGISSYLAWYQQKPGKAPKLLIYAASTLQSGVPSRFSGSGSGTDFTLTISSLQPEDFATYYCQQSYSTPFTFGQGTKVEIK
'''
jobname = 'antibody_Fv'
model_type = "alphafold2_multimer_v3"
pair_mode = "paired"
```

### Example 5: Higher-Order Complex (Trimer)

```python
query_sequence = '''
SEQUENCE1:SEQUENCE2:SEQUENCE3
'''
jobname = 'trimer_complex'
model_type = "alphafold2_multimer_v3"
pair_mode = "paired"
num_recycles = 20
use_dropout = True
num_seeds = 2
```

## Structure Analysis Pipeline

### Example 6: Analyze AlphaFold Prediction

**Step 1:** Run structure prediction in `AlphaFold2.ipynb`

**Step 2:** Download the `.pdb` file

**Step 3:** Upload to `Proteinstellar_.ipynb`

**Results:**
- Secondary structure assignment
- Misfolding detection
- Phi/Psi angle analysis
- FASTA sequence extraction
- BLAST homology search

### Example 7: Validate Experimental Structure

```python
# Upload experimental PDB from RCSB
# Example: 6RZ3 (p53 bound to DNA)

# Expected output:
# ✅ No significant misfolding detected
# 🔗 Top BLAST hits to other p53 structures
```

## Cancer Research Applications

### Example 8: EGFR Kinase Domain

**Sequence:** EGFR kinase domain (residues 696-1022)

```python
query_sequence = '''
FKKIKVLGSGAFGTVYKGLWIPEGEK-VKIPVAIKELREATSPKANKEILDEAYVMASVDNPHVCRLLGICLTSTVQLITQLMPFGCLLDYVREHKDNIGSQYLLNWCVQIAKGMNYLEDRRLVHRDLAARNVLVKTPQHVKITDFGLAKLLGAEEKEYHAEGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTFGSKPYDGIPASEISSILEKGERLPQPPICTIDVYMIMVKCWMIDADSRPKFRELIIEFSKMARDPQRYLVIQGDERMHLPSPTDSNFYRALMDEEDMDDVVDADEYLIPQQGFFSSPSTSRTPLLSSLSATSNNSTVACIDRNGLQSCPIKEDSFLQRYSSDPTGALTEDSIDDTFLPVPEYINQSVPKRPAGSVQNPVYHNQPLNPAPSRDPHYQDPHSTAVGNPEYLNTVQPTCVNSTFDSPAHWAQKGSHQISLDNPDYQQDFFPKEAK
'''
jobname = 'EGFR_kinase'
template_mode = "pdb100"
num_recycles = 6
```

**Applications:**
- Drug binding site analysis
- Mutation effect prediction
- Inhibitor design

### Example 9: Mutant p53 Analysis

```python
# Wild-type p53 DBD
query_sequence_wt = '''
SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENL
'''

# R175H mutation (hotspot mutation in cancer)
query_sequence_mut = '''
SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVHHCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENL
'''

# Compare pLDDT profiles
# Mutant likely shows lower confidence in DNA-binding region
```

## Advanced Configurations

### Example 10: Sampling Uncertainty

```python
query_sequence = 'YOUR_SEQUENCE'
jobname = 'uncertainty_sampling'

# Sample from model uncertainty
use_dropout = True
num_seeds = 5
max_msa = "64:128"

# This generates 5 diverse predictions
# Analyze ensemble for flexible regions
```

### Example 11: Custom MSA

**Step 1:** Generate MSA externally (e.g., HHblits)

**Step 2:** Upload A3M file

```python
msa_mode = "custom"
# Upload your .a3m file when prompted
```

**A3M Format:**
```
>query
MSEQVENCE...
>hit1
-SEQ-ENCE...
>hit2
MSEQVEN-E...
```

### Example 12: Template-Based Prediction

```python
query_sequence = 'YOUR_SEQUENCE'
jobname = 'template_pred'
template_mode = "custom"

# Upload PDB/mmCIF templates
# Templates must match naming: xxxx.pdb or xxxx.cif
# Better for homology modeling
```

### Example 13: Fast Screening Mode

```python
query_sequence = 'YOUR_SEQUENCE'
jobname = 'fast_screen'

# Minimal settings for quick screening
num_relax = 0
num_recycles = 1
max_msa = "32:64"
save_all = False

# Runtime: ~2-3 minutes per sequence
# Good for initial screening
```

### Example 14: High-Accuracy Mode

```python
query_sequence = 'YOUR_SEQUENCE'
jobname = 'high_accuracy'

# Maximum accuracy settings
template_mode = "pdb100"
num_recycles = 20
recycle_early_stop_tolerance = 0.5
num_relax = 5
relax_max_iterations = 2000
save_all = True
save_recycles = True

# Runtime: 20-30 minutes
# Best for final predictions
```

## Batch Processing

### Example 15: Multiple Sequences

```bash
# Create CSV file: sequences.csv
id,sequence
protein1,MSEQVENCE...
protein2,TSEQVENCE...
protein3,ASEQVENCE...

# Upload CSV as queries_path
```

## Output Analysis

### Example 16: Interpreting PAE Plots

```python
# After prediction:
# - Dark blue regions: High confidence (well-ordered)
# - Yellow/green regions: Lower confidence
# - For complexes: Check interface regions
# - Diagonal should be dark blue (self-alignment)
```

### Example 17: Quality Assessment Checklist

```python
# Good prediction indicators:
# ✓ pLDDT > 70 in functional regions
# ✓ PAE < 5 Å at protein interfaces
# ✓ pTMscore > 0.7 overall
# ✓ MSA depth > 30 sequences/position
# ✓ Consistent across multiple seeds

# Poor prediction indicators:
# ✗ pLDDT < 50 in core regions
# ✗ PAE > 15 Å at interfaces
# ✗ pTMscore < 0.5
# ✗ MSA depth < 10 sequences
# ✗ High variance between seeds
```

## Tips and Best Practices

1. **Start simple:** Test with known structures first
2. **Check MSA:** Good MSA = good prediction
3. **Use templates:** For homologs with known structures
4. **Validate:** Compare with experimental data when available
5. **Iterate:** Adjust parameters based on initial results
6. **Save everything:** Use `save_all = True` for important predictions
7. **Document:** Keep track of parameters used

## Additional Resources

- [AlphaFold FAQ](https://alphafold.ebi.ac.uk/faq)
- [ColabFold GitHub](https://github.com/sokrypton/ColabFold)
- [RCSB PDB](https://www.rcsb.org/) - Validate predictions
- [UniProt](https://www.uniprot.org/) - Protein sequences
