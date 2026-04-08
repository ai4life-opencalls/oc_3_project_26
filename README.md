<p align="center">
  <a href="https://ai4life.eurobioimaging.eu/open-calls/">
    <img src="https://github.com/ai4life-opencalls/.github/blob/main/AI4Life_banner_giraffe_nodes_OC.png?raw=true" width="70%">
  </a>
</p>

# Project #26: Automatic Microtubule Doublet Picking in Cryo-ET Tomograms

Automated pipeline for detecting and orienting microtubule doublets in cryo-electron tomograms of axonemes, with correct polarity assignment for downstream subtomogram averaging in RELION.

## Background

Cilia and flagella are built around a highly conserved structure called the **axoneme**, composed of nine microtubule doublets arranged radially around a central pair. Each doublet consists of an A-tubule and a B-tubule fused together, and the proteins that decorate them repeat at defined periodicities along the axoneme (8, 16, 24, 48, or 96 nm).

To resolve these proteins by cryo-electron tomography (cryo-ET) and subtomogram averaging, it is necessary to:

1. Precisely **locate each doublet** in 3D space
2. **Sample along its length** at regular intervals
3. Assign the **correct polarity** (all doublets pointing in the same direction)
4. Export **particle positions and orientations** for direct import into RELION

Currently, this process is performed manually using IMOD and custom scripts — a bottleneck that limits throughput and introduces inter-user variability, particularly in polarity assignment.

## Goals

- **Automate** the detection and tracing of all 9 microtubule doublets in a tomogram
- **Correctly assign polarity** to each doublet (tip-to-base orientation)
- **Sample along each doublet** and compute the 3D orientation angles at each position
- **Export a RELION-compatible particle star file** ready for subtomogram averaging
- Reduce manual intervention to zero for standard axoneme datasets

The pipeline is split into two main stages: **interactive label generation** and **automated 3D segmentation**.

```
Raw tomogram
     │
     ▼
┌─────────────────────┐
│   nnInteractive     │  ← sparse user clicks → dense 3D labels
│  (label generation) │
└────────┬────────────┘
         │  training masks
         ▼
┌─────────────────────┐
│     3D U-Net        │  ← learns to segment doublets from labelled data
│   (segmentation)    │
└────────┬────────────┘
         │  binary segmentation mask
         ▼
┌─────────────────────┐
│  Post-processing    │  ← skeletonisation, polarity assignment,
│  & export           │     sampling, angle computation
└────────┬────────────┘
         │
         ▼
  RELION star file
```
### Stage 1 — Interactive labelling with nnInteractive

[nnInteractive](https://github.com/MIC-DKFZ/nnInteractive) is used to generate high-quality 3D training labels from a small number of user interactions (point clicks or scribbles), without requiring manual segmentation of every voxel.

### Stage 2 — 3D U-Net segmentation

A [Biapy](https://github.com/BiaPyX/BiaPy) **3D U-Net** is trained on the nnInteractive-generated labels to produce a fully automated segmentation model.

- Input: raw or deconvolved tomogram (`.mrc`)
- Output: multi-class segmentation mask — one label per doublet (1–9) + background
- The network learns the appearance of doublets across different tomograms, noise levels, and orientations
- Once trained, inference runs without any user input

### Stage 3 — Post-processing and RELION export

From the segmented mask, the following steps are applied automatically:

1. **Skeletonisation** — reduce each segmented doublet to a 1D centreline in 3D
2. **Polarity assignment** — use the known 9-fold symmetry of the axoneme cross-section and the characteristic A/B tubule geometry to assign a consistent tip-to-base orientation to each doublet
3. **Sampling** — place particle positions at regular intervals along each centreline (configurable spacing, e.g. every 8 nm)
4. **Angle computation** — compute the three Euler angles (rot, tilt, psi) at each position to align the doublet to a common reference frame
5. **RELION export** — write a `.star` file with particle coordinates, angles, and tomogram metadata directly importable into RELION 4/5

## Data example
<img width="359" height="309" alt="Screenshot 2026-02-09 at 11 06 35" src="https://github.com/user-attachments/assets/ba5ac37f-07a1-4fa4-95d6-946e9afc9b09" />

<img width="272" height="400" alt="mt" src="https://github.com/user-attachments/assets/db3b67e1-7e94-4e88-aa99-7330e59ca0fa" />

  <em>On the left, a cross-section showing 9 doublets arranged in circle around central pair of microtubules (here the tip of the cilium is pointing into the page). On the rigth, the image of data along the length of the axoneme/microtubule doublets (longitudinal section along the axoneme).

## Initial Results

https://github.com/user-attachments/assets/9029d688-78dd-4be9-8d14-a2aaa4f0717a

**Figure 1 | Interactive microtubule doublet labelling using nnInteractive.**
A user provides sparse point clicks on a cryo-ET tomogram cross-section; nnInteractive
propagates these into dense 3D segmentation masks covering all 9 microtubule doublets
of the axoneme. Labels are generated in a fraction of the time required for manual
annotation and serve as training data for the downstream 3D U-Net segmentation model.


<br><br>
---
<img src="eu_flag.jpg" height="50" align="left" style="margin: 5px 10px 0 0">
<div style="text-align: justify">AI4Life has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement number 101057970. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them.</div>
