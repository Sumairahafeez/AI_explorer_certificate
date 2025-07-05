#!/bin/bash

# List of dates you want to appear in your GitHub heatmap (format: YYYY-MM-DD)
dates=(
  "2025-04-22"
  "2025-04-23"
  "2025-04-24"
  "2025-04-25"
  "2025-04-26"
  "2025-04-27"
   # Monday
)

# Optional: Set your name and email (match GitHub!)
export GIT_AUTHOR_NAME="Sumairahafeez"
export GIT_AUTHOR_EMAIL="sumairahafeezfp@gmail.com"
export GIT_COMMITTER_NAME="sumairahafeezfp@gmail.com"
export GIT_COMMITTER_EMAIL="sumairahafeezfp@gmail.com"

# Loop through each date and create a backdated commit
for date in "${dates[@]}"; do
  for i in 1 2 ; do
    hour=$((9 + i * 2))  # e.g., 11AM and 13PM
    export GIT_AUTHOR_DATE="$date T$hour:00:00"
    export GIT_COMMITTER_DATE="$date T$hour:00:00"
    git commit --allow-empty -m "Commit $i for $date" --date "$date T$hour:00:00"
  done
done

# Push all commits
git push origin main