#!/bin/bash

# List of dates you want to appear in your GitHub heatmap (format: YYYY-MM-DD)
dates=(
  "2025-01-01"
  "2025-01-02"
  "2025-01-03"
  "2025-01-04"
  "2025-01-05"  # Monday
)

# Optional: Set your name and email (match GitHub!)
export GIT_AUTHOR_NAME="Sumairahafeez"
export GIT_AUTHOR_EMAIL="sumairahafeezfp@gmail.com"
export GIT_COMMITTER_NAME="sumairahafeezfp@gmail.com"
export GIT_COMMITTER_EMAIL="sumairahafeezfp@gmail.com"

# Loop through each date and create a backdated commit
for date in "${dates[@]}"; do
  export GIT_AUTHOR_DATE="$date 12:00:00"
  export GIT_COMMITTER_DATE="$date 12:00:00"
  git commit --allow-empty -m "Heatmap filler for $date"
done

# Push all commits
git push origin main