from datetime import datetime
import random

emojis = ["🔥", "🌟", "🚀", "📅", "✍️", "✅", "🧠", "📈", "💻", "📚"]
messages = [
    "Daily log update",
    "Keep pushing!",
    "Coding streak continues",
    "Today I learned...",
    "Consistent grind",
    "Small steps daily",
    "Let's go!",
]

now = datetime.now()
emoji = random.choice(emojis)
message = random.choice(messages)

log_entry = f"{emoji} {message} on {now.strftime('%Y-%m-%d %H:%M:%S')}\n"

with open("log.txt", "a") as file:
    file.write(log_entry)

with open("today-i-learned.md", "a") as til:
    til.write(f"- {now.strftime('%Y-%m-%d')}: Placeholder for something I learned today. {emoji}\n")