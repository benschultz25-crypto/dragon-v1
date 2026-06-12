import os
import time
import math
import sys
from getpass import getpass
from colorama import Fore, Style, init
import random

init(autoreset=True)

# =========================
# LOGIN DATA
# =========================

ADMIN_USER = "admin"
ADMIN_PASS = "dragon123"

VALID_KEYS = [
    "DRAGON-ADMIN-001",
    "DRAGON-ADMIN-002",
    "DRAGON-ADMIN-003"
]

# =========================
# DRAGON ASCII Art
# =========================

dragon = r"""
                                           /===-_---~~~~~~~~~------____
                                          |===-~___                _,-'
               -==\\                         `//~\\   ~~~~`---.___.-~~
           ______-==|                         | |  \\           _-~`
     __--~~~  ,-/-==\\                        | |   `\        ,'
  _-~       /'    |  \\                      / /      \      /
.'        /       |   \\                   /' /        \   /'
/  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~
                  \_|      /        _)   ;  ),   __--~~
                    '~~--_/      _-~/-  / \   '-~ \
                   {\__--_/}    / \\_>- )<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |   _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |
                 o-o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
"""

menu = [
    "💻 Payload Generator",
    "🌐 Network Scanner",
    "🐉 Dragon Core",
    "🔥 Fire Breath",
    "📁 System Logs",
    "🔐 Encryption Center",
    "⚙ Settings",
    "❌ Exit"
]

# =========================
# FUNCTIONS
# =========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def neon(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def color_text(text, color=Fore.GREEN):
    return color + text + Style.RESET_ALL

def draw_dragon():
    t = time.time() * 6
    for y, line in enumerate(dragon.splitlines()):
        output = ""
        for x, char in enumerate(line):
            r = int(128 + 127 * math.sin(t + x * 0.12))
            g = int(128 + 127 * math.sin(t + x * 0.12 + 2))
            b = int(200 + 55 * math.sin(t + x * 0.08))
            output += neon(r, g, b) + Style.BRIGHT + char
        print(output + "\033[0m")


def login():
    clear()
    draw_dragon()
    print()
    print(color_text("╔══════════════════════════════════════════════╗", Fore.CYAN))
    print(color_text("║           DRAGON CYBER SECURITY             ║", Fore.CYAN))
    print(color_text("╚══════════════════════════════════════════════╝", Fore.CYAN))
    print("\n[ AUTHENTICATION REQUIRED ]")
    print("[ DRAGON CORE LOCKED ]")
    print("[ LICENSE VERIFICATION ENABLED ]")
    print("\n══════════════════════════════════════════════")
    user = input("\nUsername    : ")
    password = getpass("Password    : ")
    key = input("License Key : ")

    if (
        user != ADMIN_USER
        or password != ADMIN_PASS
        or key not in VALID_KEYS
    ):
        print("\n" + color_text("[ ACCESS DENIED ]", Fore.RED))
        time.sleep(3)
        raise SystemExit

    print("\n" + color_text("[ ACCESS GRANTED ]", Fore.GREEN))
    loading = [
        "[+] Verifying credentials...",
        "[+] Validating license...",
        "[+] Loading Dragon Core...",
        "[+] Initializing Neural Engine...",
        "[+] Establishing Secure Connection...",
        "[+] Dragon Core Ready..."
    ]
    for line in loading:
        print(color_text(line, Fore.YELLOW))
        time.sleep(0.4)
    time.sleep(1)

def bootscreen():
    clear()
    boot = [
        "[+] Initializing Dragon Core...",
        "[+] Loading Neural Modules...",
        "[+] Verifying Encryption Keys...",
        "[+] Connecting Secure Network...",
        "[+] Firewall Activated...",
        "[+] Dragon AI Online."
    ]
    print(color_text("\nDRAGON CYBER CORE BOOT\n", Fore.CYAN))
    for line in boot:
        print(color_text(line, Fore.YELLOW))
        time.sleep(0.4)
    time.sleep(1)

def fire_breath():
    frames = [
        "🔥",
        "🔥🔥🔥",
        "🔥🔥🔥🔥🔥",
        "🔥🔥🔥🔥🔥🔥🔥",
        "🔥🔥🔥🔥🔥🔥🔥🔥🔥",
        "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",
        "🔥🔥🔥🔥🔥🔥🔥🔥🔥",
        "🔥🔥🔥🔥🔥🔥",
        "🔥🔥🔥",
        "🔥"
    ]
    for frame in frames:
        clear()
        draw_dragon()
        print("\n" + " " * 55 + color_text(frame, Fore.RED))
        time.sleep(0.12)

    input("\nPress ENTER...")

def fake_logs():
    clear()
    logs = [
        color_text("[INFO] Dragon Core initialized", Fore.GREEN),
        color_text("[INFO] Secure channel established", Fore.GREEN),
        color_text("[INFO] Neural engine active", Fore.GREEN),
        color_text("[WARNING] Unauthorized probe blocked", Fore.YELLOW),
        color_text("[INFO] Encryption key rotated", Fore.GREEN),
        color_text("[INFO] System stable", Fore.GREEN)
    ]
    for log in logs:
        print(log)
        time.sleep(0.4)
    input("\nPress ENTER...")

def payload_generator():
    clear()
    # Animation
    print(color_text("Loading Payload Generator...", Fore.CYAN))
    for i in range(5):
        print(f"{color_text('[+]', Fore.YELLOW)} Generating payloads{'.' * (i%3+1)}")
        time.sleep(0.5)
    print("\n[+] Payload Generator is now operational.")
    print("Generate custom payloads for testing or exploitation.")
    input("\nPress ENTER to return to menu.")

def network_scanner():
    clear()
    print(color_text("Initializing Network Scanner...", Fore.CYAN))
    for i in range(3):
        print(f"{color_text('[+]', Fore.YELLOW)} Scanning subnet... ({i+1}/3)")
        time.sleep(0.5)
    print("[+] Found 3 active devices: 192.168.1.10, 192.168.1.15, 192.168.1.20")
    print("Scanning ports and vulnerabilities...")
    time.sleep(1)
    print(color_text("[+] Scan complete. No threats detected.", Fore.GREEN))
    input("\nPress ENTER to return to menu.")

def dragon_core():
    clear()
    print(color_text("Checking Dragon Core...", Fore.CYAN))
    for i in range(3):
        print(f"{color_text('[+]', Fore.YELLOW)} Powering up modules... ({i+1}/3)")
        time.sleep(0.5)
    print("[+] Dragon Core is ONLINE.")
    print("[+] Neural network active and synchronized.")
    input("\nPress ENTER to return to menu.")

def system_logs():
    fake_logs()

def encryption_center():
    clear()
    print(color_text("Accessing Encryption Center...", Fore.CYAN))
    for i in range(3):
        print(f"{color_text('[+]', Fore.YELLOW)} Initializing encryption protocols... ({i+1}/3)")
        time.sleep(0.5)
    print("[+] Encryption algorithms ready.")
    print("[+] AES-256, RSA, ECC actively secured.")
    input("\nPress ENTER to return to menu.")

def settings():
    clear()
    print(color_text("Loading Settings...", Fore.CYAN))
    for i in range(3):
        print(f"{color_text('[+]', Fore.YELLOW)} Loading configuration... ({i+1}/3)")
        time.sleep(0.5)
    print("[+] Settings menu is under construction.")
    print("[+] Future updates planned.")
    input("\nPress ENTER to return to menu.")

# =========================
# Action with random events and risk levels
# =========================

def trigger_random_event():
    events = [
        ("Hostile countermeasures detected!", "high"),
        ("Data transfer error!", "medium"),
        ("Unwanted traffic detected!", "low"),
        ("Unknown virus found!", "high"),
        ("Connection interrupted!", "medium"),
        ("Firewall blocked the attack.", "low")
    ]
    event, level = random.choice(events)
    print(f"!!! {event} !!!")
    show_alarm(level)

def show_alarm(level):
    alarms = {
        "low": Fore.CYAN + "[LOW RISK]",
        "medium": Fore.YELLOW + "[MEDIUM RISK]",
        "high": Fore.RED + "[HIGH RISK! POLICE ALERT POSSIBLE!]"
    }
    print(alarms.get(level, Fore.WHITE + "[UNKNOWN RISK]"))

def action_with_action_and_risk(action_func, action_name):
    print(color_text(f"\nInitiating {action_name}...", Fore.MAGENTA))
    print_progress("Executing...", 2)
    # Random chance for an event
    if random.random() < 0.4:
        trigger_random_event()
    else:
        print(color_text(f"{action_name} completed successfully.", Fore.GREEN))
    print()
    input("Press ENTER to continue...")

def print_progress(text, duration=2):
    """Simulate a progress bar."""
    print(text)
    for _ in range(20):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / 20)
    print()

# =========================
# Main menu functions
# =========================

def main_menu():
    menu_options = [
        ("Payload Generator", lambda: action_with_action_and_risk(payload_generator, "Payload Generator")),
        ("Network Scanner", lambda: action_with_action_and_risk(network_scanner, "Network Scanner")),
        ("Dragon Core", lambda: action_with_action_and_risk(dragon_core, "Dragon Core")),
        ("Fire Breath", lambda: action_with_action_and_risk(fire_breath, "Fire Breath")),
        ("System Logs", lambda: action_with_action_and_risk(system_logs, "System Logs")),
        ("Encryption Center", lambda: action_with_action_and_risk(encryption_center, "Encryption Center")),
        ("Settings", lambda: action_with_action_and_risk(settings, "Settings")),
        ("Exit", lambda: sys.exit())
    ]

    while True:
        clear()
        draw_dragon()
        print()
        print(color_text("╔══════════════════════════════════════════════╗", Fore.CYAN))
        print(color_text("║           DRAGON CYBER CORE v1.0            ║", Fore.CYAN))
        print(color_text("╚══════════════════════════════════════════════╝", Fore.CYAN))
        print("\n[ SYSTEM ONLINE ]")
        print("[ DRAGON CORE ACTIVE ]")
        print("[ FIREWALL STATUS: SECURE ]")
        print("[ ENCRYPTION: AES-256 ]")
        print("\n══════════════════════════════════════════════")
        for idx, (name, _) in enumerate(menu_options, start=1):
            print(f"[{idx}] {name}")
        print("══════════════════════════════════════════════")
        choice = input("\nroot@dragon:~# ")

        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            _, action = menu_options[int(choice) - 1]
            action()
        else:
            print("\n" + color_text("Invalid command.", Fore.RED))
            time.sleep(1)

# =========================
# Start
# =========================

try:
    login()
except SystemExit:
    clear()
    print(color_text("\n[ DRAGON CORE OFFLINE ]", Fore.RED))
    print(color_text("[ CONNECTION TERMINATED ]", Fore.RED))
    sys.exit()

bootscreen()
main_menu()

# On exit
clear()
print(color_text("\n[ DRAGON CORE OFFLINE ]", Fore.RED))
print(color_text("[ CONNECTION TERMINATED ]", Fore.RED))