# Reddit User Persona Generator 🤖🧠

This project takes any Reddit user profile URL and generates a detailed **User Persona** by:
- Scraping their posts & comments using the Reddit API (via PRAW)
- Summarizing behavioral traits, occupation, interests, tone, frustrations, etc.
- Providing **citations** for each trait directly from their posts/comments
- Using LLaMA-3 via the **Groq API** to build accurate personas

🔍 This was built as part of an internship evaluation task.

---

## 🔧 Features

- ✅ Accepts any Reddit profile URL
- ✅ Scrapes recent posts and comments via Reddit API
- ✅ Automatically generates a full persona using an LLM (LLaMA-3)
- ✅ Quotes Reddit comments as **citations** to support each trait
- ✅ Saves output as clean `.txt` files (1 per user)
- ✅ Works with any Reddit username (not limited to provided examples)

---

## 🚀 Technologies Used

- Python 3.9+
- [PRAW](https://praw.readthedocs.io/) for Reddit scraping
- [Groq](https://console.groq.com/) API with LLaMA-3 for persona generation
- `openai` client (used for Groq compatibility)
- `dotenv` for secure API key management

---

## 📁 Folder Structure

reddit-user-persona/
├── reddit_persona.py
├── kojied_raw.txt
├── kojied.txt
├── Hungry-Move-6603.txt
├── Hungry-Move-6603_raw.txt      
├── .env.example               
├── README.md
└── requirements.txt


## 🔐 Setup Instructions

### 1. Clone the repository

    git clone https://github.com/your-username/reddit-user-persona.git
    cd reddit-user-persona

2. Install dependencies
   pip install -r requirements.txt

3. Create a .env file
   Create a .env file in the project root folder and add your keys like this:

REDDIT_CLIENT_ID=your_reddit_app_client_id
REDDIT_CLIENT_SECRET=your_reddit_app_secret
GROQ_API_KEY=your_groq_api_key
🔑 You can create your Reddit API keys at https://www.reddit.com/prefs/apps
🔑 You can get Groq keys at https://console.groq.com

🧠 How to Run

python reddit_persona.py

When prompted:

Enter Reddit profile URL:

https://www.reddit.com/user/kojied/
✅ It will:

Scrape the user’s posts/comments

Generate a structured persona

Save the results to:

kojied_raw.txt

kojied.txt

🧪 Output Example

Username: kojied

Estimated Age: Late 20s to early 30s
> "As a matter of fact, there are a bunch of people..."

Occupation: iOS Developer
> "Hey I’m an iOS developer building in visionOS"

Interests: Technology, AR, Pokémon Go
> "I think Pokemon could be one of the killer use cases..."
✅ Each quote is cited to support the trait.

📦 Requirements
Minimal required packages:

openai==1.95.1
praw==7.8.1
python-dotenv==1.1.1

Installed using:

pip install -r requirements.txt

👤 Examples Supported
You can use:

https://www.reddit.com/user/kojied/

https://www.reddit.com/user/Hungry-Move-6603/

Or any valid Reddit user profile URL

📜 License

MIT License — you may reuse this project with credit.


🙋‍♂️ Author

Made by Suraj Agarwal
If selected, I am happy to contribute this and build further features!


🧠 Notes

This project uses Groq LLaMA-3 API via the openai Python SDK (pointing to Groq's endpoint).

Output matches persona structure shown in example image (traits, citations, tone, etc.)

Output files are saved per user and not overwritten.