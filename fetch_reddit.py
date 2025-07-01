import feedparser

# RSS URL for Reddit: Top posts of the week from r/businessanalyst
RSS_URL = "https://www.reddit.com/r/businessanalyst/top/.rss?t=week"

# Parse the feed
feed = feedparser.parse(RSS_URL)

# Filter logic: Pick first useful post
for entry in feed.entries:
    title = entry.title
    link = entry.link
    summary = entry.summary

    if len(summary) > 100:
        print("✅ Title:", title)
        print("🔗 Link:", link)
        print("📝 Summary:", summary)
        break
