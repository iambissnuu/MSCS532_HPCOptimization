# HPC Optimization Project: Structure of Arrays & Vectorization

## Overview

This project explores a fundamental optimization technique in High-Performance Computing (HPC): transforming data layout from an Array of Structs (AoS) to a Structure of Arrays (SoA), combined with vectorized computation using NumPy. The technique enhances memory locality and leverages CPU vectorization capabilities to deliver significant performance improvements.

The project fulfills *Optimization in High-Performance Computing* by implementing the selected optimization, evaluating its performance, and writing a detailed APA-style report.

---

## Optimization Technique

The optimization technique used here involves:
- **Data Layout Transformation**: From AoS to SoA to improve spatial locality.
- **Vectorization**: Using NumPy's array broadcasting and ufuncs to execute operations in compiled C instead of interpreted Python loops.


