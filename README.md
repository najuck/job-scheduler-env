---
title: Job Scheduler Environment
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: Dockerfile
pinned: false
---

# Job Scheduler Environment

## Description
This environment simulates job scheduling in a cloud system.

## State
- time
- cpu usage
- jobs

## Action
- select job id

## Reward
+1 → on-time completion  
-0.5 → delay  
-1 → overload  

## Run
pip install -r requirements.txt  
python baseline.py
The environment includes task difficulty levels and a grading system that maps performance to a 0.0–1.0 score.