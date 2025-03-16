import re
import os

TEMPLATE_DIR = "templates"  # Path to your HTML templates

# Regex pattern to find static file references in href or src attributes
pattern = re.compile(r'(href|src)=["\'](css|js|assets|img)/([^"\']+)["\']')

def replace_static_paths(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace static paths with Flask's url_for(), ensuring proper formatting
    updated_content = pattern.sub(r'\1="{{ url_for(\'static\', filename=\'\2/\3\') }}"', content)

    # Remove unnecessary escape characters (\)
    updated_content = updated_content.replace("\\'", "'")  # Fixing single quotes
    updated_content = updated_content.replace('\\"', '"')  # Fixing double quotes

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

# Loop through all HTML files in the template directory
for root, _, files in os.walk(TEMPLATE_DIR):
    for file in files:
        if file.endswith(".html"):
            replace_static_paths(os.path.join(root, file))

print("Static paths updated successfully!")
