import sys, time, random

# ANSI color codes
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}

def typing(text: str, delay: float = 0.05):
    """Print text with typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color(text: str, color: str = "white") -> str:
    """Return text in given color."""
    return f"{COLORS.get(color, COLORS['white'])}{text}{COLORS['reset']}"

def rainbow(text: str):
    """Print text in rainbow colors."""
    rainbow_colors = ["red", "yellow", "green", "cyan", "blue", "purple"]
    for i, char in enumerate(text):
        sys.stdout.write(color(char, rainbow_colors[i % len(rainbow_colors)]))
    sys.stdout.write(COLORS["reset"] + "\n")

def glitch(text: str, duration: float = 1.5):
    """Print text with glitch effect for given duration."""
    end_time = time.time() + duration
    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*")
    while time.time() < end_time:
        glitched = "".join(random.choice(chars) for _ in range(len(text)))
        sys.stdout.write("\r" + glitched)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\r" + text + "\n")
