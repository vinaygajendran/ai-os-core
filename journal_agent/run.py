from ollama import Client
from datetime import datetime
import os

def run_journal_agent():
    today = datetime.now().date()
    summary_path = f"data/journal/{today}_summary.txt"
    journal_path = f"data/journal/{today}_journal.md"

    if not os.path.exists(summary_path):
        print("[Journal Agent] No summary file found for today.")
        return

    with open(summary_path, "r", encoding="utf-8") as f:
        summary_text = f.read()

    prompt = f"""
You are a journaling assistant AI. Given the following time-tracking data, write a brief personal journal entry summarizing the day. Include what the user spent the most time on, any patterns you notice, and suggestions if any.

=== BEGIN SUMMARY ===
{summary_text}
=== END SUMMARY ===

Keep it concise and natural.
"""

    print("[Journal Agent] Contacting local LLM...")
    client = Client()
    response = client.chat(model="qwen2.5", messages=[{"role": "user", "content": prompt}])
    journal_entry = response['message']['content']

    with open(journal_path, "w", encoding="utf-8") as f:
        f.write(journal_entry)

    print(f"📝 Journal entry saved to {journal_path}")
    print("\n" + journal_entry)
