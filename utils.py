import os
import re

def clean_text(text):
    return re.sub(r"<.*?>", "", text).replace("\n", " ").strip()

def save_markdown(username, content):
    os.makedirs("output", exist_ok=True)
    filename = f"output/newsletter_{username.lower().split()[0]}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
