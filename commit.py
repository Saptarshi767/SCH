from datetime import datetime
import random

# 🎯 Emoji & Message Pool
emojis = ["🔥", "🌟", "🚀", "📅", "✍️", "✅", "🧠", "📈", "💻", "📚"]
messages = [
    "Daily log update",
    "Keep pushing!",
    "Coding streak continues",
    "Today I learned...",
    "Consistent grind",
    "Small steps daily",
    "Let's go!",
    "Pushing progress!",
    "Never give up!",
    "Stay consistent 💪"
]

# 🕓 Current Timestamp
now = datetime.now()
emoji = random.choice(emojis)
message = random.choice(messages)

# 📝 Write to log.txt
with open("log.txt", "a") as file:
    file.write(f"{emoji} {message} on {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

# 📚 Write to today-i-learned.md
with open("today-i-learned.md", "a") as til:
    til.write(f"- {now.strftime('%Y-%m-%d')}: Placeholder for something I learned today. {emoji}\n")

# ✅ Optional console output (useful for debugging in GitHub Actions log)
print(f"Committed message: {message} with {emoji}")
