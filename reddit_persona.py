import os
import re
import praw
from dotenv import load_dotenv
from openai import OpenAI

# Load .env variables
load_dotenv()

# Setup Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Setup Reddit API (PRAW)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="RedditPersonaScript/0.1 by YourRedditUsername"
)

# -------- Step 1: Input Profile URL --------
profile_url = input("Enter Reddit profile URL : ").strip()

def extract_username_from_url(url):
    match = re.search(r"reddit\.com/user/([^/]+)/?", url)
    return match.group(1) if match else "unknown_user"

username = extract_username_from_url(profile_url)
print(f"🔍 Extracted username: {username}")

# -------- Step 2: Scrape Reddit Content --------
print("🕵️ Scraping user posts and comments...")

user = reddit.redditor(username)
raw_file = f"{username}_raw.txt"

with open(raw_file, "w", encoding="utf-8") as f:
    f.write(f"--- POSTS by u/{username} ---\n\n")
    for post in user.submissions.new(limit=100):
        f.write(f"[POST] {post.title}\n{post.selftext}\n\n")

    f.write(f"--- COMMENTS by u/{username} ---\n\n")
    for comment in user.comments.new(limit=100):
        f.write(f"[COMMENT] {comment.body}\n\n")

print(f"✅ Saved scraped content to {raw_file}")

# -------- Step 3: Load Content --------
with open(raw_file, "r", encoding="utf-8") as f:
    user_data = f.read()

# Trim to 4000 chars to fit LLM limit
trimmed_data = user_data[:4000]

# -------- Step 4: Prompt LLaMA-3 via Groq --------
print("💡 Generating persona with citations...")

prompt = f"""
You are a professional UX researcher and behavioral analyst.

Based on the Reddit posts and comments below, create a **detailed user persona** for the Redditor **{username}**.

📌 The persona should follow this format:

---

**Username:**  
**Estimated Age:**  
**Occupation or Education:**  
**Location Clues:**  
**Hobbies and Interests:**  
**Personality Traits:**  
**Communication Style:**  
**Goals and Motivations:**  
**Pain Points / Frustrations:**  
**Technology Habits:**  
**Communities They Engage In:**  
**Overall Insight (Archetype):**

---

After writing the full persona, add a section:

### 🔍 Supporting Quotes for Each Section

List relevant quotes from the Reddit content that justify the persona elements above.

Only use information present in the Reddit posts/comments.

--- START OF USER CONTENT ---
{trimmed_data}
--- END OF USER CONTENT ---
"""

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

persona_output = f"Username: {username}\n\n" + response.choices[0].message.content

# -------- Step 5: Save Final Output --------
output_file = f"{username}.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(persona_output)

print(f"✅ Persona saved to: {output_file}")
