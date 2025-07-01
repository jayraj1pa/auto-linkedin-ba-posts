import requests
import os

# Use OpenRouter DeepSeek key from GitHub secret
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def rewrite_reddit_post(original_text):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://deepseek.openrouter.ai",
        "X-Title": "RedditToLinkedInBot"
    }

    prompt = f"""
    Rewrite the following Reddit post for LinkedIn:
    
    1. Make it look like a professional post.
    2. Include a thoughtful response (as if you're an expert).
    3. Use emojis, short paragraphs, a warm tone, and a call-to-action at the end.
    4. Keep it under 1200 characters.

    Reddit Post:
    {original_text}
    """

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        rewritten = result["choices"][0]["message"]["content"]
        print("🔁 Rewritten LinkedIn Post:\n", rewritten)
        return rewritten
    else:
        print("❌ Error:", response.status_code, response.text)
        return None

# TEMP: Sample post (replace later with dynamic Reddit input)
if __name__ == "__main__":
    reddit_sample = "I'm transitioning into a business analyst role and I don't know how to explain gaps in my resume. What’s the best way to show transferable skills in interviews?"
    rewrite_reddit_post(reddit_sample)
