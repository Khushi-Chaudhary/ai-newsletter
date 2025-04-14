import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

import feedparser
from transformers import pipeline
from utils import clean_text, save_markdown

# Load summarization pipeline
summarize = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_newsletter(user):
    articles = []
    
    for url in user["feeds"]:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # Limit to top 3 articles per feed
            text = clean_text(entry.get("summary", "")[:1000])
            if not text.strip():
                continue
            try:
                summary = summarize(text)[0]["summary_text"]
            except Exception as e:
                summary = "Summary generation failed."

            if any(kw.lower() in summary.lower() for kw in user["interests"]):
                articles.append({
                    "title": entry.title,
                    "summary": summary,
                    "link": entry.link
                })

    # Generate Markdown content
    content = f"# {user['name']}'s Personalized Newsletter\n\n## 🔥 Top Picks\n\n"
    if articles:
        for art in articles:
            content += f"### {art['title']}\n{art['summary']}\n[Read more]({art['link']})\n\n"
    else:
        content += "No relevant articles found based on your interests today.\n\n"

    # Save to markdown file
    save_markdown(user['name'], content)

    # Return content so Streamlit can show it
    return content
