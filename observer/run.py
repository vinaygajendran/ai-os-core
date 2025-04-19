import time
import json
import psutil
import win32gui
import win32process
import os
from datetime import datetime
from observer.parser import load_log_file, summarize_sessions, format_summary_table
from datetime import datetime


LOG_PATH = "data/logs"
INTERVAL = 2  # seconds

def get_active_window_info():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        window_title = win32gui.GetWindowText(hwnd)
        return {
            "timestamp": datetime.now().isoformat(),
            "process": process.name(),
            "window_title": window_title
        }
    except Exception as e:
        return {
            "timestamp": datetime.now().isoformat(),
            "process": "Unknown",
            "window_title": "Unknown",
            "error": str(e)
        }

def start_observer():
    print("[Observer] System tracking started. Press Ctrl+C to stop.")
    os.makedirs(LOG_PATH, exist_ok=True)

    last_title = ""
    session = {}

    try:
        while True:
            info = get_active_window_info()
            title = info["window_title"]

            if title != last_title:
                if session:
                    session["end_time"] = datetime.now().isoformat()
                    session["duration_sec"] = (
                        datetime.fromisoformat(session["end_time"]) -
                        datetime.fromisoformat(session["start_time"])
                    ).total_seconds()

                    # Log to file
                    log_file = os.path.join(LOG_PATH, f"{datetime.now().date()}.jsonl")
                    with open(log_file, "a", encoding="utf-8") as f:
                        f.write(json.dumps(session) + "\n")

                    # Print to terminal
                    print(f"\n🪟 Window: {session['window_title']}")
                    print(f"🔧 Process: {session['process']}")
                    print(f"⏱️ Duration: {int(session['duration_sec'])} sec")

                session = {
                    "start_time": info["timestamp"],
                    "window_title": info["window_title"],
                    "process": info["process"]
                }

                last_title = title

            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\n[Observer] Stopped by user.")

        # 📊 Auto-generate summary
        log_path = os.path.join(LOG_PATH, f"{datetime.now().date()}.jsonl")
        data = load_log_file(log_path)
        summary = summarize_sessions(data)
        report = format_summary_table(summary)

        print("\n" + report)

        # 📝 Save summary to file
        summary_path = f"data/journal/{datetime.now().date()}_summary.txt"
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"\n✅ Summary saved to {summary_path}")

