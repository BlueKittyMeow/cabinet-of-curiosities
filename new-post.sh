#!/bin/bash

# Usage: ./new-post.sh "Post Title" "category"
# Example: ./new-post.sh "Wicked vs Very in Newburyport" "lexical-variation"

TITLE="$1"
CATEGORY="$2"
DATE=$(date '+%Y-%m-%d')
TIME=$(date '+%Y-%m-%d %H:%M')
FILENAME="${DATE}-$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g').html"

# Create the post file
cat > "posts/$FILENAME" << EOF
<!DOCTYPE html>
<html>
<head>
    <title>$TITLE - Cabinet of Curiosities</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>$TITLE</h1>
    <p><strong>Posted:</strong> $TIME | <strong>Category:</strong> $CATEGORY</p>
    <hr>
    
    <p>Your post content goes here...</p>
    
    <hr>
    <p><a href="../index.html">← Back to all posts</a></p>
</body>
</html>
EOF

echo "Created: posts/$FILENAME"
echo "Don't forget to update index.html!"