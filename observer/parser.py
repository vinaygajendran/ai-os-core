import json
from datetime import datetime
from collections import defaultdict

def load_log_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f.readlines() if line.strip()]

def summarize_sessions(entries):
    summary = defaultdict(float)

    for entry in entries:
        process = entry.get("process", "Unknown")
        duration = entry.get("duration_sec", 0)
        summary[process] += duration

    return sorted(summary.items(), key=lambda x: -x[1])  # descending by time spent

def format_summary_table(process_data):
    lines = ["📊 Time Spent by Application", "-" * 30]
    for process, seconds in process_data:
        minutes = round(seconds / 60, 2)
        lines.append(f"{process:<20} {minutes} min")
    return "\n".join(lines)

if __name__ == "__main__":
    path = f"data/logs/{datetime.now().date()}.jsonl"
    print(f"\n[Parser] Reading from {path}...")

    data = load_log_file(path)
    summary = summarize_sessions(data)
    report = format_summary_table(summary)

    print("\n" + report)
