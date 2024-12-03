import os
import re
import sys
import subprocess
import argparse

# Define the base URL
base_url = "https://raw.githubusercontent.com/fskelly/cloud.fskelly.com/main/static/"

# Regular expression to find Hugo figure shortcodes
figure_url_pattern = re.compile(r'{{<\s*figure\s+src="([^"]+)"\s+alt="([^"]+)"\s*>}}')

# Regular expression to find commented sections
comment_pattern = re.compile(r'<!--(.*?)-->', re.DOTALL)

def update_image_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove commented sections temporarily
    comments = comment_pattern.findall(content)
    for i, comment in enumerate(comments):
        content = content.replace(comment, f"COMMENT_PLACEHOLDER_{i}")

    # Update image URLs
    def replace_url(match):
        relative_url = match.group(1)
        alt_text = match.group(2)
        new_url = base_url + relative_url
        return f'{{{{< figure src="{new_url}" alt="{alt_text}" >}}}}'

    content = figure_url_pattern.sub(replace_url, content)

    # Restore commented sections
    for i, comment in enumerate(comments):
        content = content.replace(f"COMMENT_PLACEHOLDER_{i}", comment)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def commit_changes(file_path):
    subprocess.run(["git", "add", file_path], check=True)
    subprocess.run(["git", "commit", "-m", f"Update image URLs in {file_path}"], check=True)

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update image URLs in a markdown file.")
    parser.add_argument("file_path", help="Path to the markdown file.")
    parser.add_argument("--commit", action="store_true", help="Commit the changes to git.")
    args = parser.parse_args()

    if not os.path.isfile(args.file_path):
        print(f"File not found: {args.file_path}")
        sys.exit(1)

    update_image_urls(args.file_path)
    print(f"Updated image URLs in {args.file_path}")

    if args.commit:
        commit_changes(args.file_path)
        print(f"Committed changes for {args.file_path}")