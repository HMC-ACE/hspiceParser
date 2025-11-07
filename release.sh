#!/usr/bin/env bash

set -euo pipefail

# Generate tag name with today's date (format: v2025.11.05)
TAG_NAME="v$(date +%Y.%m.%d)"

echo "Creating release tag: $TAG_NAME"

# Check if tag exists and delete it if it does
if git tag -l "$TAG_NAME" | grep -q "$TAG_NAME"; then
    echo "Tag $TAG_NAME already exists. Removing it..."
    git tag -d "$TAG_NAME"
    # Also delete from remote if it exists
    git push origin ":refs/tags/$TAG_NAME" 2>/dev/null || true
fi

# Create and push the new tag
git tag "$TAG_NAME"
git push origin "$TAG_NAME"

# Create/update the 'latest' tag to point to this release
echo "Creating/updating 'latest' tag..."
# Remove existing 'latest' tag if it exists
if git tag -l "latest" | grep -q "latest"; then
    git tag -d "latest"
    git push origin ":refs/tags/latest" 2>/dev/null || true
fi

# Create new 'latest' tag pointing to the same commit as the dated tag
git tag "latest"
git push origin "latest"

# Create GitHub release using gh CLI
echo "Creating GitHub release..."
gh release create "$TAG_NAME" \
    --title "Release $TAG_NAME" \
    --notes "Automated release for $(date +%Y-%m-%d)" \
    --latest

echo "Release $TAG_NAME created successfully!"
echo "Tag 'latest' now points to $TAG_NAME"
