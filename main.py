from observer.run import start_observer
from journal_agent.run import run_journal_agent

def main():
    print("Starting AI OS Core...")
    start_observer()
    run_journal_agent()

if __name__ == "__main__":
    main()
