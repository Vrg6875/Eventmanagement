#!/bin/bash

# Merge the feature branch
git merge feature2

# Check for merge conflicts
if [ $? -ne 0 ]; then
    echo "Conflict detected. Resolving using 'theirs' strategy..."
    git ls-files -u | awk '{print $4}' | sort -u | while read file; do
        git checkout --theirs "$file"
        git add "$file"
    done
    git commit -m "Auto-resolved conflicts using 'theirs' strategy"
fi
