🧠 README.md for ai-os-core
markdown
Copy
Edit
# AI OS Core

**AI OS Core** is a privacy-first, local-first AI operating layer for Windows that learns from your daily desktop activity to assist you through intelligent agents — powered entirely by on-device LLMs.

> ⚙️ No chat window.  
> 🧠 No cloud dependency.  
> Just intelligence that watches, learns, and helps.

---

## 🚀 What It Does

- ✅ Installs a **System Observer Agent** to track user behavior: open apps, window titles, time spent, and more.
- ✅ Logs activity in a structured format (locally).
- ✅ Installs a local LLM (via [Ollama](https://ollama.com)) — e.g., Qwen 2.5B — for semantic processing.
- ✅ Runs an intelligent **Journal Agent** that summarizes daily activity into a personal journal using your private LLM.

All data stays local. You control what is tracked and what is generated.

---

## 🧱 Project Structure

```bash
/observer        → Tracks apps, windows, activity
/journal_agent   → Generates daily summaries using LLM
/llm             → Runs and connects to local LLM (Ollama)
/data            → Stores logs and generated journals
/installer       → Scripts and assets for .exe installer
💡 How It Works
Installer sets up:

Python environment

Observer Agent (background task)

Ollama + Qwen 2.5B

Observer logs user activity (e.g., "Chrome - Gmail | 10:03 AM - 10:17 AM")

Journal Agent runs daily:

Collects logs

Sends to LLM with summarization prompt

Generates .md or .txt daily journal

User gets an intelligent, private timeline of their work.

📦 Installation
Windows-only (for now)

Coming soon:

.exe installer package (with embedded Python + Ollama setup)

Auto-start service for observer and agents

Toggle for clipboard/browser tracking

📄 License
MIT License — open to use, build, and improve.
Pull requests welcome. Let’s build the future of Personal AI together.

🤝 Contributing
💬 Want to build agents? Improve tracking? Integrate with tools like Notion, Outlook, or VS Code?

Join us!
Create a new /agents/your_agent folder and follow the contribution guide (coming soon).

🌟 What's Next?
📌 GUI Tray Manager

🧠 Custom Embedding Index

✉️ Email Assistant Agent

🔄 Daily Timeline Visualizer

🔐 Optional encrypted storage mode

🧩 Modular agent plugin system

🧠 Setting Up the Local LLM (Qwen 2.5B via Ollama)
AI OS Core uses Ollama to run the LLM locally — no internet or cloud APIs needed.
The default model used is Qwen 2.5B, which is lightweight and fast for journaling tasks.

📦 Step 1: Install Ollama
Download and install Ollama for Windows from:

👉 https://ollama.com/download

Once installed, test it:

bash
Copy
Edit
ollama --version

🧠 Step 2: Pull the Qwen Model
In your terminal, run:

bash
Copy
Edit
ollama pull qwen:2.5b
This will download the model and get it ready for use.

You can test it with:

bash
Copy
Edit
ollama run qwen:2.5b
You should see a prompt to start chatting with the model locally.

🤖 Step 3: Let the Journal Agent Use It
When you run python main.py, the Journal Agent automatically:

Reads your system usage logs

Builds a prompt for Qwen

Sends it via Ollama’s local server

Writes the journal to data/journal/YYYY-MM-DD_journal.md

No chat window, no OpenAI key, no privacy risk — just your own on-device LLM.


