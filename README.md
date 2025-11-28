# Experimental Verification of Relativistic Time Dilation via Atmospheric Muon Flux Analysis

![Project Status](https://img.shields.io/badge/Status-Completed-success) ![License](https://img.shields.io/badge/License-MIT-blue) ![Python](https://img.shields.io/badge/Python-3.9%2B-yellow)

## 📌 Abstract
This project establishes a low-cost, field-deployable methodology for verifying Special Relativity using atmospheric muons. By constructing a custom CMOS-based particle detector and conducting a vertical transect expedition in the Annapurna Sanctuary (Nepal), we measured muon flux across an altitude gradient of 3,300 meters. The results demonstrate a **3.2x increase** in flux at 4,130m compared to 822m, providing experimental evidence for relativistic time dilation.

---

## 📂 Repository Structure
```text
├── src/
│   ├── detector.py       # Real-time particle detection script (OpenCV)
│   └── analysis.py       # Data plotting and curve fitting script
├── data/
│   ├── raw_logs/         # Raw CSV logs from each expedition node
│   └── summary_data.csv  # Cleaned flux vs. altitude dataset
├── docs/
│   ├── hardware_guide.md # Instructions for building the detector
│   └── research_paper.pdf # Full technical report
└── results/
    ├── figures/          # Generated graphs (Flux vs Altitude)
    └── photos/           # Field expedition photos
