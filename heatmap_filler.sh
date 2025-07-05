#!/bin/bash

# List of dates you want to appear in your GitHub heatmap (format: YYYY-MM-DD)
dates=(
  "2025-01-10"
  "2025-01-11"
  "2025-01-13"
  "2025-01-14"
  "2025-01-15" 
  "2025-01-16" 
  "2025-01-17" 
  "2025-01-18" 
  "2025-01-19" 
  "2025-01-20" 
  "2025-01-21" 
  "2025-01-22" 
  "2025-02-01" 
  "2025-02-03" 
  "2025-02-04" 
  "2025-02-06" 
  "2025-02-08" 
  "2025-02-09" 
  "2025-02-12" 
  "2025-02-13" 
  "2025-02-14" 
  "2025-02-15" 
  "2025-02-16" 
  "2025-02-17" 
  "2025-02-18" 
  "2025-02-19" 
  "2025-02-20" 
  "2025-02-25" 
  "2025-02-27" 
  "2025-02-28" 
  "2025-02-29" 
   # Monday
)

# Optional: Set your name and email (match GitHub!)
export GIT_AUTHOR_NAME="Sumairahafeez"
export GIT_AUTHOR_EMAIL="sumairahafeezfp@gmail.com"
export GIT_COMMITTER_NAME="sumairahafeezfp@gmail.com"
export GIT_COMMITTER_EMAIL="sumairahafeezfp@gmail.com"

# Loop through each date and create a backdated commit
for date in "${dates[@]}"; do
  for i in 1 2; do
    hour=$((9 + i * 2))  # e.g., 11AM and 13PM
    export GIT_AUTHOR_DATE="$date T$hour:00:00"
    export GIT_COMMITTER_DATE="$date T$hour:00:00"
    git commit --allow-empty -m "Commit $i for $date" --date "$date T$hour:00:00"
  done
done

# Push all commits
git push origin main