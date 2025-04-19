AI OS Core

AI OS Core is a privacy-first, local-first AI operating layer for Windows that observes your system activity,
learns your behavior over time, and assists you through intelligent, local LLM-powered agents.

No chat window. No cloud dependency. Just intelligence that watches, learns, and helps — all on your machine.

What It Does

- Installs a System Observer Agent that tracks your desktop activity: apps, windows, timestamps, and interaction patterns.
- Logs all observations locally in a structured format.
- Installs and runs a local LLM (e.g., Qwen 2.5B) using Ollama.
- Launches the first agent: the Journal Agent, which generates a daily journal summarizing your activity using the private LLM.

Everything is offline and stays within your device. You own your data. You control what’s stored and what’s processed.

Project Structure

ai-os-core/
  - observer/: System observer agent (runs in background)
  - journal_agent/: Daily summarizer using LLM
  - llm/: Local LLM integration (via Ollama)
  - data/: Logs and generated journal entries
    - journal/
  - installer/: .exe installer scripts and assets
  - config/: Settings and flags
  - main.py: Entry point to orchestrate system
  - README.md

What It Tracks

- Active application/process
- Window titles and duration
- Time spent per app or task
- (Optional) Clipboard activity or browser tabs (configurable)

First Agent: The Journal Agent

The Journal Agent runs once per day (or on-demand) and:
1. Reads your system activity logs.
2. Sends them to a local LLM with a summarization prompt.
3. Writes a clean .md or .txt summary to your journal folder.

Example Output

2025-04-18 – Daily Journal

You worked primarily in Excel (Budget_Rev1.xlsx) from 9:45 AM to 11:10 AM.
You had 2 long email sessions with clients.
You browsed research papers on agent architectures for 45 minutes.
You were focused for 6.5 hours with minimal context-switching.
Reflection: Great progress on deep work. Avoid afternoon distractions tomorrow.

Installation (Coming Soon)

Windows-only (for now)

We’re working on:
- .exe installer via Inno Setup
- Embedded Python environment
- Automatic startup registration
- Ollama + Qwen 2.5 download during install
- Background process launcher for observer + agent

License

MIT License – Open for personal, professional, and commercial use.
Build, fork, and share freely. Contributions welcome!

Contributing

We’re designing an OS layer for intelligent personal computing — and we want your help.

Want to contribute?
- Add new AI agents (/agents/)
- Improve the observer (/observer/)
- Plug into local knowledge bases
- Build email, browser, or automation extensions

A full CONTRIBUTING.md and roadmap is coming soon.

Roadmap

- Phase 1 | System Observer Agent (activity logging)
- Phase 2 | LLM Setup (Ollama + local Qwen/Mistral)
- Phase 3 | Journal Agent (daily summarization)
- Phase 4 | Email Agent (contextual writing + scheduling)
- Phase 5 | GUI Tray App, visual dashboard
- Phase 6 | Plugin framework for new agents
- Future  | Encrypted memory, opt-in cloud sync

Why This Matters

AI OS Core is not a chatbot. It’s not a wrapper. It’s the first step toward a truly personal AI —
one that learns from you, lives on your machine, and actually helps.

Get Involved

Let’s build the future of personal intelligence together.

Start by cloning the repo, running the observer, and sharing your ideas. Feel free to create issues, forks, or PRs.

git clone https://github.com/your-username/ai-os-core
