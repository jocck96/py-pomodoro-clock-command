import time

def run_timer(minutes):
    seconds = minutes * 60
    for i in range(seconds):
        time.sleep(1)
        pct = int(((i + 1) / seconds) * 100)
        bar = "#" * (pct // 5) + "-" * (20 - (pct // 5))
        print(f"\rProgress: [{bar}] {pct}%", end="")
    print("\nTimer complete!")

if __name__ == "__main__":
    print("Starting 1-minute Pomodoro focus session...")
    run_timer(1)
