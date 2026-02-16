<p align="center">
  <a href="https://ai4life.eurobioimaging.eu/open-calls/">
    <img src="https://github.com/ai4life-opencalls/.github/blob/main/AI4Life_banner_giraffe_nodes_OC.png?raw=true" width="70%">
  </a>
</p>

# Project #26: Automatic microtubule doublet picking in tomograms
## Project Overview

This project aimed to average over a large number of microtubule doublets that have all been aligned to get structural information. Axonemes isolated from cilia were collected trough cryo-electron tomography. 
Proteins of interest have different periodicities along axoneme (e.g. some might bind every 96 nm and others every 8 nm, 16 nm, 24 nm, or 48 nm).   

## Goals
- Automatically detect and pick microtubule doublets with the correct polarity (i.e. all pointing the same direction) in Cryo-EM tomograms of cilia. 
- For each point along microtubule, provide angles to align the doublet for further Subtomogram averaging (STA). 

## Data example
<img width="359" height="309" alt="Screenshot 2026-02-09 at 11 06 35" src="https://github.com/user-attachments/assets/ba5ac37f-07a1-4fa4-95d6-946e9afc9b09" />

<img width="272" height="400" alt="mt" src="https://github.com/user-attachments/assets/db3b67e1-7e94-4e88-aa99-7330e59ca0fa" />

  <em>On the left, a cross-section showing 9 doublets arranged in circle around central pair of microtubules (here the tip of the cilium is pointing into the page). On the rigth, the image of data along the length of the axoneme/microtubule doublets (longitudinal section along the axoneme).

## Strategy

In order to detect the microtubule doublets we will use a set of annotations coming from manual reconstruction to train a variational autoencoder with a segmented Gaussian splat decoder to capture structural features on the tomograms. After extraction of the align particles, we will perfom a final refinement using the software Relion. 
  





<br><br>
---
<img src="eu_flag.jpg" height="50" align="left" style="margin: 5px 10px 0 0">
<div style="text-align: justify">AI4Life has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement number 101057970. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them.</div>
