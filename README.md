# NBA Clutch Player Analysis

This project looks at how NBA players perform when the game is on the line. Using play-by-play data, custom metrics, and visual tools, it highlights who truly delivers in clutch situations and how their performance stacks up against peers.

---

## Project Overview
Basketball is more than numbers, but data can tell powerful stories. Here, the focus is on late-game pressure moments—who takes the shots, who converts, and who makes the right plays when it matters most. The repository includes scripts to collect and process data, models that score player performance, and visualizations that make the results easy to explore.

---

## What’s Inside
- **data/**: Cleaned datasets with clutch stats, player IDs, and combined game logs.  
- **notebooks/**: Jupyter notebooks for exploring data and testing ideas.  
- **src/**: Core scripts:  
  - `analysis/metric_design.py` – builds custom clutch performance metrics  
  - `analysis/validation_plots.py` – generates validation and comparison visuals  
  - `data/fetch_clutch_data.py` – retrieves clutch-time play data  
  - `data/fetch_full_game_logs.py` – collects full game logs  
  - `data/merge_clutch_full.py` – merges datasets into final analysis tables  
- **NBA CLUTCH PLAYER ANALYSIS.pbix**: Power BI dashboard for interactive review of results.

---

## Key Features
1. Pulls and processes clutch-time data from NBA game logs  
2. Designs new metrics to rank and compare players under pressure  
3. Produces plots to check and explain results  
4. Provides an interactive Power BI dashboard to explore trends by player, team, and season  

---

## Getting Started
Clone the repository and install requirements:
```bash
git clone https://github.com/<your-username>/NBA-Clutch-Player-Analysis.git
cd NBA-Clutch-Player-Analysis
pip install -r requirements.txt
