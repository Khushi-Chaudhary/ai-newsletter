import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

import feedparser
from transformers import pipeline
from utils import clean_text, save_markdown

summarize = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_newsletter(user):
    articles = []
    for url in user["feeds"]:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            text = clean_text(entry.get("summary", "")[:1000])
            if not text.strip():
                continue
            summary = summarize(text)[0]["summary_text"]
            if any(kw.lower() in summary.lower() for kw in user["interests"]):
                articles.append({
                    "title": entry.title,
                    "summary": summary,
                    "link": entry.link
                })

    content = f"# {user['name']}'s Personalized Newsletter\n\n## 🔥 Top Picks\n\n"
    for art in articles:
        content += f"### {art['title']}\n{art['summary']}\n[Read more]({art['link']})\n\n"

    save_markdown(user['name'], content)
