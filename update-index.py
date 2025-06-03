#!/usr/bin/env python3

import os
import re
from datetime import datetime
import glob

def extract_post_info(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract title from <title> tag
    title_match = re.search(r'<title>(.*?) - Cabinet of Curiosities</title>', content)
    title = title_match.group(1) if title_match else "Untitled"
    
    # Extract date and category from the post
    meta_match = re.search(r'<strong>Posted:</strong> (.*?) \| <strong>Category:</strong> (.*?)</p>', content)
    if meta_match:
        date_str, category = meta_match.groups()
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
    else:
        date_obj = datetime.now()
        category = "uncategorized"
    
    return {
        'title': title,
        'date': date_obj,
        'category': category,
        'filename': os.path.basename(filepath)
    }

# Get all posts
posts = []
for filepath in glob.glob('posts/*.html'):
    posts.append(extract_post_info(filepath))

# Sort by date (newest first)
posts.sort(key=lambda x: x['date'], reverse=True)

# Generate index.html
html_content = '''<!DOCTYPE html>
<html>
<head>
    <title>Cabinet of Curiosities</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Musings of a Blue Kitty with Infinite Curiosity</h1>
    <p><em>Art, Language, Poetry, and Miscellany</em></p>
    
    <h2>Recent Posts</h2>
'''

# Group by category
categories = {}
for post in posts:
    cat = post['category']
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(post)

for category, cat_posts in categories.items():
    html_content += f'\n    <h3>{category.replace("-", " ").title()}</h3>\n    <ul>\n'
    for post in cat_posts:
        date_str = post['date'].strftime('%Y-%m-%d')
        html_content += f'        <li><strong>{date_str}</strong> - <a href="posts/{post["filename"]}">{post["title"]}</a></li>\n'
    html_content += '    </ul>\n'

html_content += '''
</body>
</html>'''

with open('index.html', 'w') as f:
    f.write(html_content)

print("Updated index.html with", len(posts), "posts")